# -*- coding: utf-8 -*-

from app import app
from flask import escape, request
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return "Привет, Flask!"
# http://127.0.0.1:5000

@app.route('/hello')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
# http://127.0.0.1:5000/hello?name=World


@app.route('/home')
def home():
    user = {'username': 'Janus'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''


@app.route('/profile')
def profile():
    user = {'username': 'Janus'}
    return render_template('index.html', title='Home', user=user)

@app.route('/blog')
def blog():
    user = {'username': 'Janus'}
    return render_template('blog.html', user=user)

@app.route('/posts')
def posts():
    user = {'username': 'Janus'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Cat'},
            'body': "Let's investigate some fish!"
        }
    ]
    return render_template('posts.html', title='All posts', user=user, posts=posts)

@app.route('/news')
def news():
    user = {'username': 'Janus'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Cat'},
            'body': "Let's investigate some fish!"
        }
    ]
    return render_template('news.html', title='All posts', user=user, posts=posts)
