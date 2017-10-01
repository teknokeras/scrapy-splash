FROM python:3.6

RUN apt-get update

RUN mkdir /code

COPY code/requirements.txt /code

WORKDIR /code

RUN apt-get install -y nano wget

RUN pip install -r requirements.txt
