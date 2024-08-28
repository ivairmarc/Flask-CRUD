from wtforms import StringField, BooleanField, validators, TextAreaField, IntegerField
from flask_wtf import FlaskForm


class NewGroup(FlaskForm):
    name = StringField('Nome', [validators.DataRequired()])
    note = TextAreaField('Observação')
    status = BooleanField('Ativo')


class PermisionsGroup(FlaskForm):
    id_group = IntegerField()
    modulo_per = StringField('Módulo')
    permission = StringField('Permissão')
    name_per = StringField('Nome da permissão')
    habilite_per = BooleanField('Habilita')
    allowcustody_per = BooleanField('Permite custódia')
    note = StringField('Observação')


class Permissions(FlaskForm):
    ...