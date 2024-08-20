from app.database import db_session
from .group_model import Groups
from flask import Blueprint 
from flask import request 
from flask import redirect 
from flask import url_for 
from flask import render_template
from flask_login import login_required


group_route = Blueprint('groups', __name__, template_folder='templates')


@group_route.route('/create', methods=['GET', 'POST'])
@login_required
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
@login_required
def list_groups():
    groups = Groups.query.all()
    return render_template('list_groups.html', groups=groups)


@group_route.route('/edit')
@login_required
def edit_group():
    ...