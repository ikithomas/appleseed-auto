FROM python:3.9-slim

ENV APP_ROOT "/app"

RUN mkdir -p $APP_ROOT
WORKDIR $APP_ROOT
COPY requirements.txt .

RUN apt-get update \
  && apt-get install -y vim iceweasel \
  && pip3 install -r requirements.txt \
  && webdrivermanager firefox chrome --linkpath /usr/local/bin
