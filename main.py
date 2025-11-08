from flask import Flask, render_template, request
from flask_navigation import Navigation
import src.calculator_functions as cf

app = Flask(__name__)
nav = Navigation(app)

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('About', 'about')
])

@app.route('/', methods=['GET', 'POST'])
def index(name=None):
    if request.method == "POST":
            return render_template('index.html')
    return render_template('index.html')

@app.route('/about', methods=['GET', 'POST'])
def index(name=None):
    if request.method == "POST":
            return render_template('about.html')
    return render_template('about.html')

app.run(debug=True)
