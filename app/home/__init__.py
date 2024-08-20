from .home import home_route


def init_app(app):
    app.register_blueprint(home_route, url_prefix='/')
    