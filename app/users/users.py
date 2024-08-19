from app.users.user_model import Users
from app.groups.group_model import Groups
from app.users.forms import NewUser
from app.database import db_session
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user
from flask import (
    Blueprint, 
    request, 
    redirect, 
    url_for, 
    render_template)


user_route = Blueprint('users', __name__, template_folder='templates')
login_manager = LoginManager()
csrf = CSRFProtect()


@login_manager.user_loader
def user_loader(id):
    user = db_session.query(Users).filter_by(id=id).first()
    return user


@user_route.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


@user_route.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@user_route.route('/create2', methods=['GET', 'POST'])
def new_user2():
    form = NewUser(request.form)

    if request.method == 'POST' and form.validate():
        
        new_user = Users(
            name=form.name.data, 
            email=form.email.data, 
            password=form.password.data, 
            status=form.status.data) 
        
        db_session.add(new_user)
        db_session.commit()

        groups_id = form.groups.data
        # Associa o usuário aos grupo selecionado
        for group_id in groups_id:
            if group_id:
                group = Groups.query.get(group_id)
                if group:
                    new_user.groups.append(group)
        db_session.commit()

        return redirect(url_for('user_route.list_users'))
    
    return render_template('new_user2.html', form=form)


@user_route.route('/create', methods=['GET', 'POST'])
def new_user():
    groups = Groups.query.all()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        status = int(request.form.get('status', 0))
        
        # Recupera o ID do grupo
        groups_id = request.form.getlist('groups')

        # Cria um novo usuario
        new_user = Users(name=name, email=email, password=password, status=status)

        db_session.add(new_user)
        db_session.commit()

        # Associa o usuário aos grupo selecionado
        for group_id in groups_id:
            if group_id:
                group = Groups.query.get(group_id)
                if group:
                    new_user.groups.append(group)
        db_session.commit()
        
        return redirect(url_for('users.list_users'))
    
    return render_template('new_user.html', groups=groups)


# para chave add /<param>
@user_route.route('/')
def list_users():
    users = Users.query.all()
    #group = Groups.query.all()
    return render_template('list_user.html', users=users)


@user_route.route('/<int:user_id>/edit', methods=['PUT'])
def update_user(user_id):
    ...


@user_route.route('/<int:user_id>/delete', methods=['DELETE'])
def delete_user(user_id):
    ...
