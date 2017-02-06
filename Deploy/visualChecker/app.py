# -*- coding: utf-8 -*-

import flask
import tornado.wsgi
import tornado.httpserver

import sys

import yweather
reload(sys)
sys.setdefaultencoding('utf8')
#########################################
# Obtain the flask app object
app = flask.Flask(__name__)
client = yweather.Client()
@app.route('/')
def index():
    # Starting point
    return flask.render_template('index.html', has_result=False)

@app.route('/run_model', methods=['POST'])
def run_model():
    text_input = flask.request.form['link_input']
    if "San Francisco" in text_input:
        imgFile = "rainy.png"
    else:
        imgFile = "sunny.jpeg"
    ### Place your function here
    output = changeText(text_input)
    return flask.render_template('index.html', has_result=True,
            result=(True, text_input,
                    text_input,
                    output,
    imgFile                  ))

def start_tornado(app, port=""):
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(app))
    http_server.listen(port)
    print("Tornado server starting on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()

def changeText(input):
    id = client.fetch_woeid(input)



if __name__ == '__main__':
    start_tornado(app, port=5012)
