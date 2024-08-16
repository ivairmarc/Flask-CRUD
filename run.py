from flask import Flask
from flask_login import LoginManager
from configuration import config_all


app = Flask(__name__)

login_manager = LoginManager(app)


if __name__ == '__main__':
    config_all(app)
    app.run()
    