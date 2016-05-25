from flask import render_template, redirect, url_for, request, jsonify,flash,session,g

from ppy import services
from ppy import forms
from . import login

#to do delete
from  ppy import models

# login
@login.route('/')
def main():
    return redirect(url_for('login.loginPage'))


@login.route('/login')
def loginPage():
    return render_template("login.html")




# @login.route("/test")
# def test():
#     user = models.User(100, "d", "p")
#     session["ssss"] = "sss"
#     print(session.__dict__)
#     #session.__setattr__("u",user)
#     session["u"] = user
#     u = session.get("u")



    print(u)
    return render_template("test.html")