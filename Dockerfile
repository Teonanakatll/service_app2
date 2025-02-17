#FROM python:3.9-alpine3.16
#
#COPY requirements.txt /temp/requirements.txt
#COPY service /service
#
#WORKDIR /service
#EXPOSE 8000
#
#RUN apk add postgresql-client postgresql-dev build-base
#RUN pip install -r /temp/requirements.txt
#RUN adduser --disabled-password service-user
#
#USER service-user

FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY service /service

WORKDIR /service
EXPOSE 8000

RUN apk add postgresql-client postgresql-dev build-base
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password service-user

USER service-user