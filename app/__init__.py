from flask import Flask
from app.database import init_db
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
    # Configuração do banco de dados
    app.config.from_object('app.config.DevelopmentConfig')
    #login_manager = LoginManager(app)
    with app.app_context():
        init_db()

    return app
