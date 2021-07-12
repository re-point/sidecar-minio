import os
import uvicorn

port = os.getenv('PORT')


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port)