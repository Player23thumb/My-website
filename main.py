# imports
from flask import Flask, render_template, request
import src.calculator_functions as cf

app = Flask(__name__)

# get html file
@app.route('/', methods=['GET', 'POST'])
def index(name=None):
    if request.method == "POST":
            return render_template('index.html')
        

    return render_template('index.html')

app.run(debug=True)
