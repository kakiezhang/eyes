# -*- encoding: utf8 -*-

from application import app
from flask import render_template, url_for

@app.route("/detail/")
def detail() :
    print 123
    return render_template("detail.html")
