
import flask
from flask import Flask, url_for, render_template, redirect

app = Flask(__name__)

@app.route('/home/')
def home():
    return render_template("basic_rendering_home.html")

@app.route('/greet/<name>/')
def greet(name):
    return render_template("basic_rendering_greet.html", name=name)

if __name__ == '__main__':

    app.run()