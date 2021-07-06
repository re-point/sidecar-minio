FROM python:3.8

COPY Pipfile .
COPY Pipfile.lock .

RUN  pip install fastapi uvicorn pipenv && \
  apt-get update && \
  apt-get upgrade -y && \
  pipenv install --system --deploy --ignore-pipfile && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y && \
  rm -rf /var/lib/apt/lists/*

COPY ./src/ ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]


