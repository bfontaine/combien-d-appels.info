# -*- coding: UTF-8 -*-

from flask import Flask, render_template, redirect, url_for
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    calls_count = "%4s" % randint(80, 8000)
    return render_template("home.html",
            calls_count=calls_count)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for("static", filename="favicon.ico"), 301)
