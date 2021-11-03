#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from bottle import Bottle
from bottle import template, request, static_file
from navi import Navi

app = application = Bottle()
navi = Navi()


@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./static")

@app.route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root=os.getcwd(), download=filename.capitalize())

@app.route('/mgr/<id:int>')
def mgr():
    return template('mgr.html')

@app.route('/login')
def login():
    return template('login.html')

@app.route("/login",method="POST")
def do_login():
    password = request.forms.get("password")
    print(password)
    print(type(password))
    if password == "Unit@123":
        print("<p>login success</p>")
    else:
        return "<h1>功能还未完善</h2>"
    return template('mgr.html')

@app.route('/')
def index():
    html_file = 'hao456.html'
    navi.generate('demo.html', html_file)
    return template(html_file)

if __name__ == '__main__':
    app.run(reloader=True, host='0.0.0.0', port=9000, debug=True)

