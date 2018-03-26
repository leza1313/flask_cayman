from flask import Blueprint,render_template, redirect, url_for, request
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
    return redirect(url_for('bajos.html'))

@bajos.route('/nuevobajo', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        foto = request.form['myfoto']
        if foto is '':
            return redirect(url_for('bajos.html'))

        mibajo = BajosModel(nombre, descripcion, foto)
        mibajo.insert_to_db()
        id = BajosModel.find_by_name(nombre).id
        fotos = int((len(request.form) - 3) / 2)

        for index in range(1, fotos+1):
            mifoto = FotosBajosModel(request.form['alt'+index.__str__()],request.form['myfoto'+index.__str__()], id)
            mifoto.insert_to_db()


    return render_template('nuevobajo.html', mytitle='Anadir Bajo')
