from flask import Blueprint, render_template
profile_bp = Blueprint('profile', __name__, url_prefix='/perfil')

@profile_bp.route('/profile')
def index():
    return render_template('profile/index.html')