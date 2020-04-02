#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:08:05 2020

@author: kclark75
"""

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '7d5866603c603ce88d35f07f9233a4ff'

posts = [
    {
         'author': 'Kenneth Clark',
         'title': 'Blog Post 1',
         'content': 'Black dude in lakeridge cures coronavirus!',
         'date_posted': 'March 28, 2020'
     },
    {
         'author': 'Jane Doe',
         'title': 'Blog Post 2',
         'content': 'Second post content',
         'date_posted': 'March 28, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
