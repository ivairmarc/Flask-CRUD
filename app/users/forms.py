from wtforms import (
    BooleanField, 
    PasswordField, 
    validators, 
    SelectMultipleField, 
    StringField
)
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email
from app.groups.group_model import Groups


class NewUser(FlaskForm):
    def __init__(self, *args, **kwargs):
        super(NewUser, self).__init__(*args, **kwargs)
        self.groups.choices = [(g.id, g.name) for g in Groups.query.all()]

    name = StringField('Nome', [validators.Length(min=4, max=30), validators.DataRequired()],  )
    email = StringField('email', [validators.Length(min=6, max=30), validators.DataRequired()], )
    password = PasswordField('Senha', [
        validators.Length(min=8, max=40),
        validators.EqualTo('confirm', message='Senha deve ser igual'), validators.DataRequired()
        ])
    confirm = PasswordField('Repita a Senha', validators=[DataRequired()])
    status = BooleanField('Ativo')
    groups = SelectMultipleField('Grupos', coerce=int, validators=[DataRequired()])
