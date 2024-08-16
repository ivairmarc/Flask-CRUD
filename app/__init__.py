from flask import Flask
from flask_login import LoginManager
from app.database import init_db
from app import (
    users, 
    groups, 
    home
)


def CreateApp():
    app = Flask(__name__)
    # Configuração do banco de dados
    
    users.init_app(app)
    groups.init_app(app)
    home.init_app(app)
    app.config.from_object('app.config.DevelopmentConfig')
    #login_manager = LoginManager(app)
    with app.app_context():
        init_db()

    return app
