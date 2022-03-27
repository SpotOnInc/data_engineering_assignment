# Docker build ingestion image
FROM python:3.8-buster
RUN apt-get update
RUN apt-get install libpq-dev -y --no-install-recommends

RUN mkdir /spoton
WORKDIR /spoton
ADD requirements.txt /spoton/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /spoton
