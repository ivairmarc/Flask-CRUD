from .views import user_route, csrf


def init_app(app):
    app.register_blueprint(user_route, url_prefix='/users')
    csrf.init_app(app)