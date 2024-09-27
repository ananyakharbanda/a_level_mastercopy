import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template('safe_filter.html', my_html='<h1>This is my HTML!</h1>')

if __name__ == '__main__':
    app.run()