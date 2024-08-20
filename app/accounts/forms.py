from wtforms import StringField, PasswordField, validators
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField('E-mail')
    password = PasswordField('Senha')