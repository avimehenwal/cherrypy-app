# -*- coding: utf-8 -*-
import cherrypy

class Root(object):

    @cherrypy.expose
    def index(self):
        """Dealing with sessions"""
        if 'count' not in cherrypy.session:
            cherrypy.session['count'] = 0
        cherrypy.session['count'] += 1
        cherrypy.log('COUNT=%s' % cherrypy.session['count'])
        return "hello world COUNT=%s" % cherrypy.session['count']

    @cherrypy.expose
    def echo(self, message):
        """HTTP/Request arguments"""
        return message

    @cherrypy.expose
    def info(self):
        """Reading from config file"""
        return cherrypy.request.app.config['avi']['name']

if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    # MOUNTING SINGLE APP
    cherrypy.quickstart(Root(), '/', 'server.conf')
