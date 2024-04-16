from app import app
from flask import render_template, session, redirect, request

@app.before_request
def set_session_language():
    if 'language' not in session:
        session['language'] = 'en'  # Set default language here


@app.route('/')
@app.route('/index')
def index():
    return (render_template("index.html"))

@app.route('/itinerary')
def itinerary():
    return (render_template ("itinerary.html"))

@app.route('/contact')
def contact():
    return (render_template ("contact.html"))

''' Adding more routes if needed '''

@app.route('/setlang/<lang_code>')
def set_language(lang_code):
#Pop the session variable to None to force an overwrite
    session.pop('language', None)
#Set the session variable lang to whatever code was used in the url
    session["language"] = lang_code
#refresh the page from which the set language request was made
    return redirect(request.referrer)