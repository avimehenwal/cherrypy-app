import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return """<html>
        <head><title> avimehenwal </title></head>
        <body> Hey and Hello world  </body>
        </html>"""

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Root())
