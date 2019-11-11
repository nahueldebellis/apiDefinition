#Python api
FROM python:latest

MAINTAINER debellisnahuel@gmail.com

WORKDIR ./api

COPY requirements.txt ./
COPY requirements.py ./

RUN pip install -r requirements.txt && python3 requirements.py

COPY . ./
