from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
  user = {'username': 'Brendan'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'First post!'
    },
    {
      'author': {'username': 'Jane'},
      'body': 'Hello, world!'
    }
  ]
  
  return render_template('index.html', title='Home', user=user, posts=posts)
