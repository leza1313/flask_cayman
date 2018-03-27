from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.promociones import PromocionesModel


promociones = Blueprint('promociones', __name__)

@promociones.route('/borrarpromocionesfoto/<string:id>')
@login_required
def borrar(id):
    url = 'https://ucarecdn.com/'+id+'/'
    mifoto = PromocionesModel.find_by_name(url)
    if mifoto:
        mifoto.delete_from_db()
        flash('Exito: Se ha eliminado correctamente la foto de promocion')
        return redirect(url_for('index'))
    flash('Error: No se ha conseguido eliminar la foto de promocion')
    return redirect(url_for('index'))

@promociones.route('/nuevapromocionesfoto', methods=['POST'])
@login_required
def nuevo():

    numfotos = int(len(request.form)/2)
    for index in range(1, numfotos+1):
        url = request.form['myfoto'+index.__str__()]
        alt = request.form['alt'+index.__str__()]
        if url is '':
            flash('Error: Es necesario seleccionar una imagen')
            return redirect(url_for('index'))
        mifoto = PromocionesModel.find_by_name(url)
        if mifoto:
            flash('Error: La foto ya esta en promociones')
        mifoto = PromocionesModel(url,alt)
        mifoto.insert_to_db()
        flash('Exito: Se ha anadido correctamente la promocion')
    return redirect(url_for('index'))
