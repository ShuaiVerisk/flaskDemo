# -*- coding: utf-8 -*-

import flask
import tornado.wsgi
import tornado.httpserver

import sys
import re
import os
reload(sys)
sys.setdefaultencoding('utf8')
#########################################
# Obtain the flask app object
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', has_result=False)

@app.route('/run_model', methods=['POST'])
def run_model():
    result_1="raw"
    return flask.render_template('index.html', has_result=True,
            result=(True, result_1,
                    ))
def start_tornado(app, port=""):
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(app))
    http_server.listen(port)
    print("Tornado server starting on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    start_tornado(app, port=5011)
