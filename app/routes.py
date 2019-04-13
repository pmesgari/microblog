from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        msg = 'Login request for user {}, remember me={}'.format(
            form.username.data,
            form.remember_me.data
        )
        flash(msg)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)