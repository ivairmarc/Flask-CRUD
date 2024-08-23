from .views import group_route, csrf


def init_app(app):
    app.register_blueprint(group_route, url_prefix='/groups')
    csrf.init_app(app)