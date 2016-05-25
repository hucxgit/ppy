# -*- coding:utf-8 -*-
from flask import request, redirect, url_for, flash,session

from ppy import models
from ppy import services

#from ppy import login_manager
from flask.ext.login import logout_user,login_user,login_required,current_user

from . import login

#login_manager.login_view = "login.loginPage"
#login_manager.login_message = u"please first login"
#login_manager.login_message_category = "info"



import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

@login.route("/settings")
@login_required
def settings():
    pass



# @login_manager.user_loader
# def load_user(user_id):
#     print("login_manager.user_loader")
#     print(user_id)
#     user = models.User(100, "admin", "admin")
#     return user
    #return session.get(user_id+"")
    #return models.User.get(user_id)
    #return models.User.get(user_id)




#login out
# @login.route('/loginoutAction',methods=['GET'])
# def loginout():
#     session.pop('username', None)
#     return redirect(url_for('login.loginPage'))


@login.route("/loginoutAction")
#@login_required
def logout():
    #logout_user()
    return redirect(url_for('login.loginPage'))



# login
@login.route("/loginAction", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = request.form.get('rememberme')

    if (username == "admin" and password == "admin"):
        #user = models.User(100,username,password)
        #login_user(user)
        #session['objects'].append(user)
        return redirect(url_for('index.index'))
    else:
       flash('账号密码不匹配')
       return redirect(url_for('login.loginPage'))

