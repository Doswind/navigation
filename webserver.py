#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from bottle import Bottle
from bottle import template, request, static_file, redirect
from navi import Navi

app = application = Bottle()
navi = Navi()

@app.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./static")

@app.route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root=os.getcwd(), download=filename.capitalize())


@app.route('/mgr', method=["POST","GET"])
def mgr():
    if request.method == 'GET':
        print('enter mgr:get')
        return template("mgr.html")
    else:
        print('enter mgr:post')
        table = request.forms
        linkname = table.get('linkname')
        linkaddr = table.get('linkaddr')
        notice = table.get('notice')
        print(linkname)
        print(linkaddr)
        print(notice)
        print(table)
        print(request)
        return template('mgr.html')

@app.route("/login", method=["POST","GET"])
def login():
    if request.method == 'GET':
        print('enter login:get')
        return template("login.html")
    else:
        print('enter login:post')
        password = request.forms.get("password")
        print(password)
        print(type(password))
        if password == "Unit@123":
            print("<p>login success</p>")
        else:
            return "<h1>功能还未完善</h2>"

        return redirect('mgr')

@app.route('/')
def index():
    html_file = 'hao456.html'
    return template(html_file, linkgroup = navi.load())

if __name__ == '__main__':
    app.run(reloader=True, host='0.0.0.0', port=9000, debug=True)

