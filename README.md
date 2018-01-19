# CHERRYPY-APP

A very basic web application using the
[CherryPy](http://cherrypy.org/) framework and Python 3.5.

The image is quite light thanks to
[Alpine Linux](https://hub.docker.com/r/frolvlad/alpine-python3/).


## App in action

### RUN

```
$ docker run --name cpy --rm -d -p 8080:8080 avimehenwal/cherrypy-app:0.4 ./app.py
```

For live logs run like

```
$ docker run --name cpy --rm -p 8080:8080 avimehenwal/cherrypy-app:0.4 helloworld.py
```

You can point your browser to http://locahost:8080/

### LOGS

```
$ docker logs cherrypy
```

### STOP

```
$ docker stop cherrypy
```


## Build it

```
$ docker build -t avimehenwal/cherrypy-app:0.5 .
```
