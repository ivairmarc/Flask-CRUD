from app.configuration import config_all
from app import CreateApp


if __name__ == '__main__':
    app = CreateApp()
    config_all(app)
    app.run()
    