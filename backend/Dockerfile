FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt