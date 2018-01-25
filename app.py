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
    cherrypy.config.update("server.conf")
    cherrypy.quickstart(Root())
