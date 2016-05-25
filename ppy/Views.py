from flask import request,redirect,session,url_for

def init_vies(app):
    @app.before_request
    def beforerequest():
        print("beforerequest")
        print(request.path)
        if (request.path == "/" or
                    request.path == "/login" or
                    request.path == "/loginAction"):
            return

        print("before bo return")
        print(request.full_path)
        username = session.get('username')
        if (username == "" or username == None):
            print("get value heheh")
            return redirect(url_for('login.loginPage'))
        pass

