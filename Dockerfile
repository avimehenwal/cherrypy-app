FROM frolvlad/alpine-python3
MAINTAINER avimehenwal

LABEL author=avimehenwal
ENV python=3
ENV webframework=cherrypy

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

#CMD ["python3", "app.py"]
ENTRYPOINT ["python3"]
