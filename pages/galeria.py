from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.galeria import GaleriaModel


galeria = Blueprint('galeria', __name__)

@galeria.route('/galeria')
def html():
    mygaleria = GaleriaModel.query.all()
    return render_template('galeria.html', mygaleria=mygaleria, mytitle='Galeria')

@galeria.route('/borrarfoto/<string:id>')
@login_required
def borrar(id):
    url = 'https://ucarecdn.com/'+id+'/'
    mifoto = GaleriaModel.find_by_name(url)
    if mifoto:
        mifoto.delete_from_db()
        flash('Exito: Se ha eliminado correctamente la foto de la galeria')
        return redirect(url_for('bajos.html'))
    flash('Error: No se ha conseguido eliminar la foto de la galeria')
    return redirect(url_for('bajos.html'))

@galeria.route('/nuevafoto', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        url = request.form['myfoto']
        alt = request.form['alt']
        if url is '':
            flash('Error: Es necesario seleccionar una imagen')
            return redirect(url_for('galeria.nuevo'))
        mifoto = GaleriaModel.find_by_name(url)
        if mifoto is None:
            mifoto = GaleriaModel(url,alt)
            mifoto.insert_to_db()
        flash('Exito: Se ha añadido correctamente el nuevo bajo')
    return redirect(url_for('galeria.html'))
