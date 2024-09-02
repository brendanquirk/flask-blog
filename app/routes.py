from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Brendan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'First post'
        },
        {
            'author': {'username': 'Jane'},
            'body': 'Second post'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

from flask import render_template, request

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)