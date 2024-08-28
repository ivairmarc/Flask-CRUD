from app.database import db_session
from .group_model import Groups, Permissions
from flask import Blueprint 
from flask import request 
from flask import redirect 
from flask import url_for 
from flask import render_template
from flask_login import login_required
from flask_wtf.csrf import CSRFProtect, CSRFError
from .forms import NewGroup, NewPermissions


group_route = Blueprint('groups', __name__, template_folder='templates')
csrf = CSRFProtect()


@group_route.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


@group_route.route('/create', methods=['GET', 'POST'])
@login_required
def new_group():
    form = NewGroup(request.form)
    if request.method == 'POST':
        name = form.name.data
        note = form.note.data
        status = form.status.data
                
        new_group = Groups(name=name, note=note, status=status)
        db_session.add(new_group)
        db_session.commit()
        
        return redirect(url_for('groups.list_groups'))
    
    return render_template('new_group.html', form=form)


@group_route.route('/')
@login_required
def list_groups():
    groups = Groups.query.all()
    return render_template('list_groups.html', groups=groups)


@group_route.route('/edit')
@login_required
def edit_group():
    ...


@group_route.route('/permission/create', methods=['GET','POST'])
@login_required
def new_permission():
    form = NewPermissions(request.form)
    if request.method == 'POST':
        module = form.module.data
        permission = form.permission.data
        name = form.name.data

        new_permission = Permissions(module=module, permission=permission,name=name)
        db_session.add(new_permission)
        db_session.commit()

        return redirect(url_for('groups.list_permissions'))
    
    return render_template('new_permission.html', form=form)


@group_route.route('/permissions')
@login_required
def list_permissions():
    permissions = Permissions.query.order_by(Permissions.module).all()
    return render_template('permissions.html', permissions=permissions)


@group_route.route('/<id>/permissiongroup', methods=['GET', 'POST'])
@login_required
def new_permission_group():
    # trazer a lista de permissões agrupados por módulo
    # pegar o id do grupo
    ...