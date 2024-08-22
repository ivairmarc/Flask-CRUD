from flask import Blueprint
from flask import render_template 
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.security import check_password_hash
from functools import wraps
from app.users.user_model import Users
from .forms import LoginForm
from app.database import db_session
from .decoratos import validate



account_route = Blueprint('login', __name__, template_folder='templates')
login_manager = LoginManager()
login_manager.login_view='login.login'
csrf = CSRFProtect()


@login_manager.user_loader
def user_loader(id):
    user = db_session.query(Users).filter_by(id=id).first()
    return user


@account_route.route('/', methods=['GET', 'POST'])
@validate
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        email = form.email.data
        password = form.password.data
        return email, password  # This is passed to the decorator for processing
               
    return render_template('login.html', form=form)


@account_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))
