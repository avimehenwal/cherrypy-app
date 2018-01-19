import cherrypy
import random
import string
import os, os.path

class StringGenerator(object):

    @cherrypy.expose
    def index(self):
        """\ index      homepage """
        return """<html>
<head>
    <link href="/static/css/style.css" rel="stylesheet">
</head>
<body>
    <form method="get" action="generate">
        <input type="text" value="8" name="length" />
        <button type="submit">Give it now!</button>
    </form>
</body>
</html>"""

    @cherrypy.expose
    def generate(self, length=8):
        """\generate?length=<>    random string generator service"""
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string

    @cherrypy.expose
    def display(self):
        """\display        HTTP session identifier"""
        return cherrypy.session['mystring']

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
