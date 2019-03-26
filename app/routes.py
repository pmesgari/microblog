from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Payam'}
    posts = [
        {
            'author': {'username': 'Payam'},
            'body': 'Sunny day in the Netherlands'
        },
        {
            'author': {'username': 'John'},
            'body': 'Satellite earth observation'
        }
    ]
    return render_template('index.html', user=user, title='Home', posts=posts)
