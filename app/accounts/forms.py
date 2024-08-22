from wtforms import StringField, PasswordField, BooleanField
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField('E-mail')
    password = PasswordField('Senha')
    remember = BooleanField()