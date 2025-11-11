from flask import Blueprint, render_template

profile_bp = Blueprint('profile', __name__, template_folder='templates')

def get_user_details():
    user_data = {
        "username": "dinaraguleia",
        "nome_completo": "Dina Raguleia",
        "email": "dina@exemplo.com",
        "bio": "A cachorrinha mais linda do mundo."
    }
    return user_data

@profile_bp.route('/profile')
def index():
    dados_usuario = get_user_details()
    return render_template('profile/index.html', user=dados_usuario)