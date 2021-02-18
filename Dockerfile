FROM python:3.8.0

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /web_hook_create

COPY . ./

RUN apt-get update -y && apt-get install -y build-essential default-libmysqlclient-dev default-mysql-client

# install dependencies
RUN pip install -U pip
#RUN pip install pipenv
RUN pip install -r requirements.txt

RUN chmod 777 -R ./
