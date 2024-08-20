from .view import group_route


def init_app(app):
    app.register_blueprint(group_route, url_prefix='/groups')