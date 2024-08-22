from flask import (
    Blueprint, 
    render_template)
from flask_login import login_required

home_route = Blueprint('home', __name__, template_folder='templates')

@home_route.route('/')
@home_route.route('/home')
@login_required
def index():
    return render_template('base.html')
