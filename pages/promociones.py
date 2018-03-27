from flask import Blueprint,render_template, request, redirect, url_for
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
    return redirect(url_for('index'))

@promociones.route('/nuevapromocionesfoto', methods=['POST'])
@login_required
def nuevo():

    numfotos = int(len(request.form)/2)
    for index in range(1, numfotos+1):
        url = request.form['myfoto'+index.__str__()]
        alt = request.form['alt'+index.__str__()]
        if url is '':
            return redirect(url_for('index'))
        mifoto = PromocionesModel.find_by_name(url)
        if mifoto is None:
            mifoto = PromocionesModel(url,alt)
            mifoto.insert_to_db()

    return redirect(url_for('index'))
