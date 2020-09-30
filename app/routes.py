from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'filippo'}
  posts = [
    {
      'author': {"username": "Filippo Rivolta"},
      'body': 'Lorem ipsum dolor sit amet'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)