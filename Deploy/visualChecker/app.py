# -*- coding: utf-8 -*-

import flask
import tornado.wsgi
import tornado.httpserver

import sys

import pyowm

reload(sys)
sys.setdefaultencoding('utf8')
#########################################
# Obtain the flask app object
app = flask.Flask(__name__)

@app.route('/')
def index():
    # Starting point
    return flask.render_template('index.html', has_result=False)

@app.route('/run_model', methods=['POST'])
def run_model():
    # Here you get what the client types in in the form
    text_input = flask.request.form['link_input']

    ### Place your function here
    imgFile, output = getWeather(text_input)
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

def getWeather(input):
    if "San Francisco".lower() in input.lower() or "London".lower() in input.lower():
        imgFile = "rainy.png"
        prediction = "There will be some rain later in the day"
    else:
        imgFile = "sunny.jpeg"
        prediction = "Open your Weather APP on the smartphone. It is way better."
    return imgFile, prediction




if __name__ == '__main__':
    start_tornado(app, port=5012)
