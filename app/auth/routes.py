from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder="auth_templates")

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route('/login')
def login():
    return render_template('login.html')