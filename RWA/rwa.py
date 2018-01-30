import sqlite3
import cherrypy
from cherrypy import tools

DB_STRING = "./resource/http_requests.db"
TABLE_NAME = "COMPANY"

class Root(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()      # tools to send json output
    def index(self):
        return "Welcome to Homepage"

@cherrypy.expose
class RestApiCollection(object):

    @cherrypy.tools.json_out()
    def GET(self):
        result = list()
        cherrypy.log("GET LIST")
        with sqlite3.connect(DB_STRING) as con:
            QUERY = "SELECT ID, NAME, AGE, ADDRESS, SALARY FROM %s" % TABLE_NAME
            cherrypy.log(QUERY)
            cursor = con.execute(QUERY)
            for row in cursor:   #tuple
                record = {
                "ID"      : row[0],
                "NAME"    : row[1],
                "AGE"     : row[2],
                "ADDRESS" : row[3],
                "SALARY"  : row[4]
                }
                result.append(record)
        cherrypy.log("GET request ready for dispatch")
        return {"results" : result}

    def POST(self):
        return "Add new collection"


@cherrypy.expose
class RestApiItems(object):

    @cherrypy.tools.json_out()
    def GET(self, id):
        cherrypy.log("RESTAPI GET ID")
        with sqlite3.connect(DB_STRING) as con:
            QUERY = "SELECT ID, NAME, AGE, ADDRESS, SALARY FROM %s WHERE ID=%s" % (TABLE_NAME, id)
            cherrypy.log(QUERY)
            cursor = con.execute(QUERY)
            record = cursor.fetchone()
            print(type(record))    # tuple
        return {"RECORD" : record}

    def PUT(self, id):
        return "Modify Item"

    def DELETE(self, id):
        return "remove Item"

    def POST(self, id):
        return "New Item"


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
        }
    }
    cherrypy.config.update("server.conf")
    cherrypy.tree.mount(Root(), '/')
    cherrypy.tree.mount(RestApiCollection(), '/collection', conf)
    cherrypy.tree.mount(RestApiItems(), '/item', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
