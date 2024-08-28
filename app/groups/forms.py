from wtforms import StringField, BooleanField, validators, TextAreaField, IntegerField
from flask_wtf import FlaskForm


class NewGroup(FlaskForm):
    name = StringField('Nome', [validators.DataRequired()])
    note = TextAreaField('Observação')
    status = BooleanField('Ativo')


class NewPermisionsGroup(FlaskForm):
    id_group = IntegerField()
    permission = StringField('Permissão')
    habilite_per = BooleanField('Habilita')
    allowcustody_per = BooleanField('Permite custódia')
    note = StringField('Observação')


class NewPermissions(FlaskForm):
    module = StringField('Módulo')
    permission = StringField('Permissão')
    name = StringField('Nome Permissão')
