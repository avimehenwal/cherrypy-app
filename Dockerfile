FROM python:3
# base ubuntu with python and bash

LABEL author=avimehenwal
ENV python=3
ENV webframework=cherrypy

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
