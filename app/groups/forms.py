from wtforms import StringField, BooleanField, validators, TextAreaField
from flask_wtf import FlaskForm


class NewGroup(FlaskForm):
    name = StringField('Nome', [validators.DataRequired()])
    note = TextAreaField('Observação')
    status = BooleanField('Ativo')


class PermisionsGroup(FlaskForm):
    ...
