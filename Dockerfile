# Docker build ingestion image
from python:3.8-buster

# Fill me in

RUN pip install kaggle
WORKDIR /code
COPY . /code
