from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuração do banco de dados
    app.config.from_object('app.config.Config')
    
    # Inicializando o SQLAlchemy
    db.init_app(app)
    
    # Registrando as rotas
    from .routes import main
    app.register_blueprint(main)
    
    return app