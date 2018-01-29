import cherrypy
import sqlite3


@cherrypy.expose
class RESTWebApp(object):

	def GET(self):
		print(cherrypy.request.headers)
		#return cherrypy.request.wsgi_environ
		return cherrypy.request.headers

if __name__ == '__main__':
	cherrypy.config.update("server.conf")
	conf = {
	    '/': {
	        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
	        'tools.sessions.on': True,
	        'tools.response_headers.on': True,
	        'tools.response_headers.headers': [('Content-Type', 'text/plain')],
	    }
	}
	cherrypy.quickstart(RESTWebApp(), '/', conf)