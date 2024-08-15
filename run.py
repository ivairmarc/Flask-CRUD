from database.database import init_db
from flask import Flask
from routes.users import user_route
from routes.groups import group_route


def create_app():
    app = Flask(__name__)
    # Registrando as rotas
    app.register_blueprint(user_route, url_prefix='/users')
    app.register_blueprint(group_route, url_prefix='/groups')
    # Configuração do banco de dados
    app.config.from_object('config.config.DevelopmentConfig')

    # Cria as tabelas no banco de dados
    with app.app_context():
        init_db()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()