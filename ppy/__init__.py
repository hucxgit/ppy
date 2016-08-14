from flask import Flask

#from flask_login import LoginManager

#login_manager = LoginManager()

#from .Views import init_vies

app = Flask(__name__);

from configs import load_config
def registerblueprint(app):
    from ad import ad as ad_blueprint
    from find import find as find_blueprint
    from Report import report as report_blueprint
    from login import login as login_blueprint
    from index import index as index_blueprint
    from Message import Message as message_blueprint
    from Image import Image as image_blueprint
    app.register_blueprint(ad_blueprint)
    app.register_blueprint(find_blueprint)
    app.register_blueprint(report_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(message_blueprint)
    app.register_blueprint(image_blueprint)


def getConfigByKey(key):
    value = app.config.get(key)
    return value


def create_app():

    print(app)
    # Load config
    config = load_config()
    app.config.from_object(config)

    #login_manager.init_app(app)
    registerblueprint(app)

    #init_vies(app)

    return app



