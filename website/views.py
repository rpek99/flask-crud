from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .dbmodels import User

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    
    return render_template("home.html", user=current_user)

@views.route('/admin')
@login_required
def admin():
    users = User.query.all()
    return render_template("admin.html",user=current_user, users = users)