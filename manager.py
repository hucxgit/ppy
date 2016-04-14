#Flask-Scripts
from flask.ext.script import Manager
#livereload
from livereload import Server

from ppy import create_app
app = create_app()

#manager
manager = Manager(app)


@manager.command
def dev():
    live_server = Server(app.wsgi_app)
    live_server.watch('templates/*.*')
    live_server.serve(open_url=True)



@manager.command
def test():
    pass
@manager.command
def development():
    pass
def production():
    pass

if __name__ == '__main__':
    print("server running")
    manager.run()
