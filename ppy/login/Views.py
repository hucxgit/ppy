from flask import render_template, redirect, url_for, request, jsonify,flash,session,g

from ppy import services
from . import login

#to do delete
from  ppy import models

# login
@login.route('/')
def main():
    return redirect(url_for('login.loginPage'))


@login.route('/login_page')
def loginPage():
    return render_template("login.html")
