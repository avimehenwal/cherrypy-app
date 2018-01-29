[![CircleCI](https://circleci.com/gh/avimehenwal/cherrypy-app/tree/master.svg?style=svg)](https://circleci.com/gh/avimehenwal/cherrypy-app/tree/master)

# CHERRYPY-APP

A very basic web application using the
[CherryPy](http://cherrypy.org/) framework and [Python 3.5](https://www.python.org/).
The image is quite light thanks to
[Official python image](https://hub.docker.com/_/python/).

## Application in action

### RUN

```
$ docker run --name cpy --rm -d -p 8081:8081 avimehenwal/auto-cherrypy-app
```

You can point your browser to http://locahost:8080/

### LOGS

```
$ docker logs --follow cpy
```

### STOP

```
$ docker stop cpy
```

## DEMO

[![asciicast](https://asciinema.org/a/159797.png)](https://asciinema.org/a/159797?speed=2)

## NOTES

To store, persist and query data you need a proper database server. There exist many to choose from with various paradigm support:

* __relational__: PostgreSQL, SQLite, MariaDB, Firebird
* __column-oriented__: HBase, Cassandra
* __key-store__: redis, memcached
* __document oriented__: Couchdb, MongoDB
* __graph-oriented__: neo4j

## ISSUES
1. Unable to run app with __cherryd__ both on local and inside docker.
python app.py - works good within container provided host and port are supplied
cherryd app.py

## SWARM DEPLOYMENT

1. Create a swarm cluster with 2 or 3 nodes
2. Deploy application as a service
3. Scale up/down
4. Install Rolling updates