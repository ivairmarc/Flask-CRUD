from wtforms import (
    BooleanField, 
    PasswordField, 
    validators, 
    SelectField, 
    StringField,

)
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from app.groups.group_model import Groups


class NewUser(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(NewUser, self).__init__(*args, **kwargs)
        self.group.choices = [(g.id, g.name) for g in Groups.query.all()]

    name = StringField('Nome', [validators.Length(min=4, max=98)])
    email = StringField('email', [validators.Length(min=6, max=98)])
    password = PasswordField('password', [
        validators.Length(min=8, max=40),
        validators.EqualTo('confirm', message='Senha deve ser igual')
        ])
    confirm = PasswordField('Repeat Password')
    status = BooleanField('Ativo')
    group = SelectField('Grupo', coerce=int, validators=[DataRequired()])
