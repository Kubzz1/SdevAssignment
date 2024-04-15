#Start of Code
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Karl'}
    labclasses = [
    {
    'weekno': 'one',
    'content': 'Getting started with Flask!'
    },

    {
    'weekno': 'two',
    'content': 'Template Inheritance!'
    }

    ]

    return render_template('index.html', pagetitle='Lab TWO', user = user, labclasses = labclasses)
#End of Code