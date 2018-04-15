from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask import current_app as app
from flask_login import login_required

from models.guitarras import GuitarrasModel
from models.fotosguitarras import FotosGuitarrasModel

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
        flash('Exito: Se ha eliminado correctamente la guitarra')
        return redirect(url_for('guitarras.html'))
    flash('Error: No se ha conseguido eliminar la guitarra')
    return redirect(url_for('guitarras.html'))

@guitarras.route('/nuevaguitarra', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descrip']
        acabado = request.form['acabado']
        pastillas = request.form['pastillas']
        puente = request.form['puente']
        electronica = request.form['electronica']
        clavijero = request.form['clavijero']
        foto = request.form['myfoto']
        if foto.__str__() is '':
            flash('Error: Es necesario seleccionar una imagen')
            return redirect(url_for('guitarras.nuevo'))

        miguitarra = GuitarrasModel(nombre, descripcion,acabado,pastillas,puente,electronica,clavijero,foto)
        miguitarra.insert_to_db()

        if 'alt1' not in request.args:
            flash('Exito: Se ha anadido correctamente la nueva guitarra')
            return redirect(url_for('guitarras.html'))

        id = GuitarrasModel.find_by_name(nombre).id
        fotos = int((len(request.form) - 3) / 2)

        for index in range(1, fotos+1):
            mifoto = FotosGuitarrasModel(request.form['alt'+index.__str__()],request.form['myfoto'+index.__str__()], id)
            mifoto.insert_to_db()
        flash('Exito: Se ha anadido correctamente la nueva guitarra')
        return redirect(url_for('guitarras.html'))

    return render_template('nuevaguitarra.html', mytitle='Anadir Guitarra')
