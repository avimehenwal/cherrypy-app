# -*- coding: utf-8 -*-
import cherrypy

class Root(object):

    @cherrypy.expose
    def index(self):
        return "hello world"

    @cherrypy.expose
    def echo(self, message):
        return message


if __name__ == '__main__':
    # The config.update is optional, but this will prevent scaling issues in a moment
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0', # 127.0.0.1 is default
        'server.socket_port': 8081, # 8080 is default
        'server.thread_pool': 100, # 10 is default
        'tools.trailing_slash.on': False # True is default
    })

    cherrypy.quickstart(Root(), '/', "prod.conf")

