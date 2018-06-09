from flask import Blueprint, render_template, redirect, url_for
from flask import request, flash
from models.user import UserModel

from werkzeug.security import check_password_hash,generate_password_hash
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
                flash('Exito: Bienvenido Administrador '+username)
                return redirect(url_for('index'))

        flash('Error: Credenciales invalidas, prueba otra vez')
        return render_template('login.html', mytitle='Login')
    return render_template('login.html', mytitle='Login')

@login.route('/nuevoAdmin', methods=['GET', 'POST'])
@login_required
def nuevoadmin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_candidate = request.form['password_candidate']

        print(username,password,password_candidate)
        print(generate_password_hash(password,method='sha256'))
        user = UserModel.query.filter_by(nombre=username).first()

        if user:
            flash('Error: El administrador ya existe')
            return redirect(url_for('login.nuevoadmin'))
        hash1=generate_password_hash(password, method='sha256')
        if not check_password_hash(hash1, password_candidate):
            flash('Error: Las contraseñas no coinciden')
            return redirect(url_for('login.nuevoadmin'))
        myUser=UserModel(username,hash1)
        myUser.insert_to_db()
        return redirect(url_for('login.nuevoadmin'))
    users=UserModel.query.all()
    return render_template('nuevoadmin.html', mytitle='Nuevo Admin',users=users)


@login.route('/borrarAdmin/<string:nombre>', methods=['GET', 'POST'])
@login_required
def borrar(nombre):
    myUser = UserModel.find_by_name(nombre)
    if myUser:
        myUser.delete_from_db()
        flash('Exito: Se ha eliminado correctamente el administrador')
        return redirect(url_for('login.nuevoadmin'))
    flash('Error: No se ha conseguido eliminar el administrador')
    return redirect(url_for('login.nuevoadmin'))
