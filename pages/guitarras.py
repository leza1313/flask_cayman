from flask import Blueprint,render_template, request, redirect, url_for
from flask import current_app as app
from flask_login import login_required

from models.guitarras import GuitarrasModel

guitarras = Blueprint('guitarras', __name__)



@guitarras.route('/guitarras')
def html():
    misguitarras = GuitarrasModel.query.all()
    return render_template('guitarras.html', guitarras=misguitarras, mytitle='Guitarras')


@guitarras.route('/borrarguitarra/<string:nombre>')
@login_required
def borrar(nombre):
    miguitarra = GuitarrasModel.find_by_name(nombre)
    if miguitarra:
        miguitarra.delete_from_db()
    return redirect(url_for('guitarras.html'))

@guitarras.route('/nuevaguitarra', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        foto = request.form['foto']

        miguitarra = GuitarrasModel(nombre,foto,foto,foto,foto,descripcion)
        #print(miguitarra)
        miguitarra.insert_to_db()

    return render_template('nuevaguitarra.html', mytitle='Añadir Guitarra')
