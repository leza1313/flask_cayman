from flask import Blueprint, render_template, redirect, url_for
from flask import request, flash
from models.user import UserModel

from werkzeug.security import check_password_hash
from flask_login import login_manager,login_required,login_user,logout_user


login = Blueprint('login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def html():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        #print(username,password_candidate)
        user = UserModel.query.filter_by(nombre=username).first()

        if user:
            if check_password_hash(user.password,password_candidate):
                login_user(user)
                return redirect(url_for('index'))

        error = 'Credenciales invalidas, prueba otra vez'
        return render_template('login.html', error=error)
    return render_template('login.html')