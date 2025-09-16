FROM python:3.13.7-slim

WORKDIR /app
COPY requirements.txt  .
RUN pip install -r requirements.txt

COPY ./app ./

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
