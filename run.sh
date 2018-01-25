#!/bin/bash
# docker kill and rm prevent funny errors
docker kill cpy > /dev/null 2>&1
docker rm cpy > /dev/null 2>&1
docker kill testcpy > /dev/null 2>&1
docker rm testcpy > /dev/null 2>&1

# build, test, and run the image
docker build -t avimehenwal/cherrypy-app:5 .
docker build -f Test_Dockerfile -t avimehenwal/test-cherrypy-app:2 .

# TEST
docker run --name testcpy --rm -it avimehenwal/test-cherrypy-app:2

# RUN
docker run -ti --name cpy -d -p 8081:8081 avimehenwal/cherrypy-app:5 $@
