import cherrypy
from cherrypy import tools


@cherrypy.expose
@cherrypy.tools.json_out()		# tools to send json output
class RESTWebApp(object):

	def GET(self):
		#return cherrypy.request.wsgi_environ
		#import ipdb; ipdb.set_trace()
		return cherrypy.request.headers

if __name__ == '__main__':
	cherrypy.config.update("server.conf")
	conf = {
	    '/': {
	        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
	        'tools.response_headers.on': True,
	    }
	}
	cherrypy.quickstart(RESTWebApp(), '/', conf)