from flask import (
    Blueprint, 
    request, 
    redirect, 
    url_for, 
    render_template)
from .models import User
from app.app import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('cadastro.html')


@main.route('/users')
def list_users():
    users = User.query.all()
    return render_template('list_users.html', users=users)