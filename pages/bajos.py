from flask import Blueprint,render_template, redirect, url_for, request, flash
from flask import current_app as app
from flask_login import login_required

from models.bajos import BajosModel
from models.fotosbajos import FotosBajosModel

bajos = Blueprint('bajos', __name__)

@bajos.route('/bajos')
def html():
    misbajos=BajosModel.query.all()
    return render_template('bajos.html', bajos=misbajos, mytitle='Bajos')

@bajos.route('/borrarbajo/<string:nombre>')
@login_required
def borrar(nombre):
    mibajo = BajosModel.find_by_name(nombre)
    if mibajo:
        mibajo.delete_from_db()
        flash('Exito: Se ha eliminado correctamente el bajo')
        return redirect(url_for('bajos.html'))
    flash('Error: No se ha conseguido eliminar el bajo')
    return redirect(url_for('bajos.html'))

@bajos.route('/nuevobajo', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descrip']
        boton = request.form['boton']
        precio = request.form['precio']
        acabado = request.form['acabado']
        pastillas = request.form['pastillas']
        puente = request.form['puente']
        electronica = request.form['electronica']
        clavijero = request.form['clavijero']
        foto = request.form['myfoto']
        if precio.__str__() is '':
            flash('Error: Es necesario introducir el precio')
            return redirect(url_for('bajos.nuevo'))

        if boton.__str__() is '':
            flash('Error: Es necesario introducir el boton de paypal')
            return redirect(url_for('bajos.nuevo'))

        if foto.__str__() is '':
            flash('Error: Es necesario seleccionar una imagen')
            return redirect(url_for('bajos.nuevo'))

        mibajo = BajosModel(nombre, descripcion,acabado,pastillas,puente,electronica,clavijero,boton,precio,foto)
        mibajo.insert_to_db()

        if 'alt1' not in request.form:
            flash('Exito: Se ha anadido correctamente el nuevo bajo')
            return redirect(url_for('bajos.html'))

        id = BajosModel.find_by_name(nombre).id
        #request.form - (number of parameters of the form that aren't photos)
        fotos = int((len(request.form) - 10) / 2)

        for index in range(1, fotos+1):
            mifoto = FotosBajosModel(request.form['alt'+index.__str__()],request.form['myfoto'+index.__str__()], id)
            mifoto.insert_to_db()
        flash('Exito: Se ha anadido correctamente el nuevo bajo')
        return redirect(url_for('bajos.html'))

    return render_template('nuevobajo.html', mytitle='Anadir Bajo')
