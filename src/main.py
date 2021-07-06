from fastapi import FastAPI

import os
from minio import Minio
import distutils.util

minio_url = os.getenv('MINIO_URL')
bucket = os.getenv('BUCKET')
minio_access_key = os.getenv('MINIO_ACCESS_KEY')
minio_secret_key = os.getenv('MINIO_SECRET_KEY')
minio_is_secure = distutils.util.strtobool(os.getenv('MINIO_IS_SECURE'))
temp_folder_path = os.getenv('TEMP_FOLDER_PATH', '/data')

minio_client = Minio(minio_url, minio_access_key, minio_secret_key, secure=minio_is_secure)

app = FastAPI()


@app.get("/", response_model=str)
def get_file(from_path: str, to_path: str):
    minio_client.fget_object(bucket, from_path, os.path.join(temp_folder_path, to_path))
    return None


@app.put("/", response_model=str)
def create_file(from_path: str, to_path: str):
    minio_client.fput_object(bucket, to_path, os.path.join(temp_folder_path, from_path))
    return None


@app.delete("/", response_model=str)
def delete_file(from_path: str):
    minio_client.remove_object(bucket, from_path)
    return None
