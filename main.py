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
    nav.Item('Qualifications', 'qualifications'),
    nav.Item('Feedback', 'feedback')
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
    qualifications = ['Chemistry (AQA, triple, higher) - grade 7', 'Physics (AQA, triple, higher) - grade 7', 'Biology (AQA, triple, higher) - grade 6', 
                               'Mathematics (Edexcel, higher) - grade 8', 'Statistics (Edexcel, higher) - grade 6', 'Further mathematics (AQA) - grade 7',
                               'Geography (AQA) - grade 6', 'English Language (AQA) - grade 7', 'English Literature (AQA) - grade 6',
                               'Spanish (Edexcel, higher) - grade 6']
    if request.method == "POST":
        return render_template('qualifications.html', qualifications_list=qualifications)
    return render_template('qualifications.html', qualifications_list=qualifications)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == "POST":
        likeThisWebsite = request.form.get('checkbox')
        opinion = request.form.get('opinion')
        if likeThisWebsite == None:
            likeThisWebsite = 'OFF'
        with open('form', 'a') as form:
            form.write(likeThisWebsite + opinion)
        return render_template('feedback.html')
    return render_template('feedback.html')

app.run(debug=True)
