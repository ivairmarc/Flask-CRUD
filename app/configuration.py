from routes.users import user_route
from routes.groups import group_route
from database.database import init_db


def config_all(app):
    config_routs(app)
    # Cria as tabelas no banco de dados
    with app.app_context():
        init_db()


def config_routs(app):
    # Registrando as rotas
    app.register_blueprint(user_route, url_prefix='/users')
    app.register_blueprint(group_route, url_prefix='/groups')

    # Configuração do banco de dados
    app.config.from_object('config.config.DevelopmentConfig')