import os
from flask import Flask
from app.database import init_db
from jinja2 import FileSystemLoader, Environment
from app import (
    users, 
    groups, 
    home
)


def CreateApp():
    app = Flask(__name__)
    
    users.init_app(app)
    groups.init_app(app)
    home.init_app(app)

    app.config.from_object('app.config.DevelopmentConfig')
    
    with app.app_context():
        init_db()

    return app
