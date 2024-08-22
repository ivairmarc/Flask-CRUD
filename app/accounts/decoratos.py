# app/decorators.py
from functools import wraps
from flask import request, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash
from flask_login import login_user
from ..users.user_model import Users  # Ajuste conforme sua estrutura
from ..database import db_session  # Ajuste conforme sua estrutura
from .forms import LoginForm


def validate(func):
    @wraps(func)
    def validate_login(*args, **kwargs):
        if request.method == 'POST':
            email, password, remember = func(*args, **kwargs)
            user = db_session.query(Users).filter_by(email=email).first()

            if user and check_password_hash(user.password, password):
                login_user(user, remember=remember)
                return redirect(url_for('home.index'))
            else:
                flash('Invalid email or password', 'danger')
                return render_template('login.html', form=LoginForm(request.form))
        return func(*args, **kwargs)
    
    return validate_login
