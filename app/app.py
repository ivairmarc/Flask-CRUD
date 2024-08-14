from flask import Flask
from flask_wtf.csrf import CSRFProtect


def create_app():
    app = Flask(__name__)
    
    # Configuração do banco de dados
    app.config.from_object('app.config.DevelopmentConfig')
    
    # Registrando as rotas
    from .routes import main
    app.register_blueprint(main)
    
    return app
