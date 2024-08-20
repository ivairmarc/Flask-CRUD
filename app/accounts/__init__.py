from .accounts import account_route, csrf, login_manager


def init_app(app):
    app.register_blueprint(account_route, url_prefix='/login')
    csrf.init_app(app)
    login_manager.init_app(app)