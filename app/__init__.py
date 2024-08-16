from flask import Flask
from flask_login import LoginManager


def CreateApp():
    app = Flask(__name__)
    #login_manager = LoginManager(app)

    return app


