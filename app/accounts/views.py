from flask import Blueprint
from flask import render_template 
from flask import request
from flask import redirect
from flask import url_for
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from werkzeug.security import check_password_hash
from app.users.user_model import Users
from .forms import LoginForm
from app.database import db_session



account_route = Blueprint('login', __name__, template_folder='templates')
login_manager = LoginManager()
login_manager.login_view='login.login'
csrf = CSRFProtect()


@login_manager.user_loader
def user_loader(id):
    user = db_session.query(Users).filter_by(id=id).first()
    return user


@account_route.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        
        result = valida_login(form.email.data, form.password.data)
        if result == True:
            
            return redirect(url_for('home.index'))
       
    return render_template('login.html', form=form)


@account_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.login'))


def valida_login(email, passwd):
    user = db_session.query(Users).filter_by(email=email).first()

    if check_password_hash(user.password, passwd):
        login_user(user)
        return True
    else:
        return False
    

def valida(func):

    def valida_login(email, passwd):
        user = db_session.query(Users).filter_by(email=email).first()

        if check_password_hash(user.password, passwd):
            login_user(user)
            return True
        
    return valida_login()
