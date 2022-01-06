import os
from bottle import Bottle
from bottle import template, request, static_file, redirect

app = Bottle()

@app.route('/boh',method=["POST","GET"])
def login():
    if request.method == "GET":
        return template('boh.html')
    else:
        u = request.forms.get('user')
        p = request.forms.get('pwd')
        return template('<b>Hello {{ name }}</b>!', name="user")

@app.route('/hello')
def index():
    # return "Hello World"
    return template('<b>Hello {{ name }}</b>!', name="user")

app.run(host='0.0.0.0',port=8080)