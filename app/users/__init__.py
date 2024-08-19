from .users import user_route, login_manager, csrf


def init_app(app):
    app.register_blueprint(user_route, url_prefix='/users')
    login_manager.init_app(app)
    csrf.init_app(app)