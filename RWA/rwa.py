import sqlite3
import cherrypy
from cherrypy import tools

DB_STRING = "./resource/http_requests.db"
TABLE_NAME = "COMPANY"

class Root(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()      # tools to send json output
    def index(self):
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


@cherrypy.expose
class RestAPI(object):

    # def _cp_dispatch(self, vpath):
    #     if len(vpath) == 2:
    #         cherrypy.request.params['id'] = vpath.pop()  # /band name/
    #         cherrypy.request.params['db_name'] = vpath.pop() # /album title/
    #         return self

    def POST(self):
        return 'post'

    @cherrypy.tools.json_out()
    def GET(self, table, id):
        cherrypy.log("RESTAPI GET ID")
        with sqlite3.connect(DB_STRING) as con:
            QUERY = "SELECT ID, NAME, AGE, ADDRESS, SALARY FROM %s WHERE ID=%s" % (table, id)
            cherrypy.log(QUERY)
            cursor = con.execute(QUERY)
            record = cursor.fetchone()
            print(type(record))    # tuple
        return {"RECORD" : record}


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
        }
    }
    cherrypy.config.update("server.conf")
    cherrypy.tree.mount(Root(), '/')
    cherrypy.tree.mount(RestAPI(), '/api', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()
