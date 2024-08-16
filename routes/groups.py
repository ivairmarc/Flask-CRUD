from database.database import db_session
from database.models.group_model import Groups
from flask import (
    Blueprint, 
    request, 
    redirect, 
    url_for, 
    render_template)


group_route = Blueprint('groups', __name__)

@group_route.route('/create', methods=['GET', 'POST'])
def new_group():
    if request.method == 'POST':
        name = request.form['name']
        note = request.form['note']
        status = request.form['status']
                
        new_group = Groups(name=name, note=note, status=status)
        db_session.add(new_group)
        db_session.commit()
        
        return redirect(url_for('groups.list_groups'))
    
    return render_template('new_group.html')


@group_route.route('/')
def list_groups():
    groups = Groups.query.all()
    return render_template('list_groups.html', groups=groups)


@group_route.route('/edit')
def edit_group():
    ...