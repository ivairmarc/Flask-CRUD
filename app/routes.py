from flask import (
    Blueprint, 
    request, 
    redirect, 
    url_for, 
    render_template)
from .models import Users, Groups
from .forms import NewUser
from app.database import db_session


main = Blueprint('main', __name__)


@main.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@main.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@main.route('/')
def index():
    return render_template('base.html')


@main.route('/users/create2', methods=['GET', 'POST'])
def new_user2():
    form = NewUser(request.form)

    if request.method == 'POST' and form.validate():
        
        user = Users(form.name.data, form.email.data, form.password.data, form.status.data, form.group.data) 

        new_user = Users(user)
        db_session.add(new_user)
        db_session.commit()
        
        return redirect(url_for('main.list_users'))
    
    return render_template('new_user2.html', form=form)


@main.route('/users/create', methods=['GET', 'POST'])
def new_user():
    groups = Groups.query.all()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        status = request.form['status']
        group = request.form['group']
        new_user = Users(name=name, email=email, password=password, status=status, group=group)
        db_session.add(new_user)
        db_session.commit()
        
        return redirect(url_for('main.list_users'))
    
    return render_template('new_user.html', groups=groups)


# para chave add /<param>
@main.route('/users')
def list_users():
    users = Users.query.all()
    return render_template('list_user.html', users=users)


@main.route('/groups/create', methods=['GET', 'POST'])
def new_group():
    if request.method == 'POST':
        name = request.form['name']
        note = request.form['note']
        status = request.form['status']
                
        new_group = Groups(name=name, note=note, status=status)
        db_session.add(new_group)
        db_session.commit()
        
        return redirect(url_for('main.list_groups'))
    
    return render_template('new_group.html')


@main.route('/groups')
def list_groups():
    groups = Groups.query.all()
    return render_template('list_groups.html', groups=groups)


@main.route('/groups/edit')
def edit_group():
    ...