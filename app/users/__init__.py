from .users import user_route


def init_app(app):
    app.register_blueprint(user_route, url_prefix='/users')