from flask import Flask, render_template, request
import src.calculator_functions as cf

# Patch old-style imports used by flask_navigation
import flask
import markupsafe
flask.Markup = markupsafe.Markup
import collections
import collections.abc
collections.MutableSequence = collections.abc.MutableSequence
collections.Iterable = collections.abc.Iterable
from flask_navigation import Navigation

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('About', 'about'),
    nav.Item('Qualifications', 'qualifications')
])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
            return render_template('index.html')
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == "POST":
            return render_template('about.html')
    return render_template('about.html')

@app.route('/qualifications', methods=['GET', 'POST'])
def qualifications():
    if request.method == "POST":
        return render_template('qualifications.html')
    return render_template('qualifications.html')

app.run(debug=True)
