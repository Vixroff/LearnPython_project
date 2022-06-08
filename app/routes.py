from flask import render_template, redirect, request, session, url_for
from app import app
from app.forms import LoginForm
from models.student import Student

@app.route('/index')
@app.route("/")
def index():
    peoples = Student
    return render_template('main_page.html', peoples=peoples)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login_page.html', title='Sign In', form=form)


