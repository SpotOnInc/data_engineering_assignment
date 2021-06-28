# Docker build ingestion image
FROM python:3.8-buster

# Fill me in

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /code
COPY . /code
