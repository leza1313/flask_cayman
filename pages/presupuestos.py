from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask import current_app as app
from flask_login import login_required
presupuestos = Blueprint('presupuestos', __name__)

from models.presupuestos import PresupuestosModel

import datetime


@presupuestos.route("/presupuestos", methods=['GET'])
@login_required
def html():
    mypresupuestos= PresupuestosModel.query.all()
    return render_template('presupuestos.html',mytitle='Presupuestos', mypresupuestos=mypresupuestos)

@presupuestos.route("/presupuestos/<string:id>", methods=['GET'])
@login_required
def info(id):
    mypresupuesto = PresupuestosModel.find_by_id(id)
    return render_template('presupuestoInfo.html',mytitle='Info Presupuesto', mypresupuesto=mypresupuesto)

@presupuestos.route("/presupuestos/borrar/<string:id>", methods=['GET'])
@login_required
def borrar(id):
    mypresupuesto = PresupuestosModel.find_by_id(id)
    if mypresupuesto:
        mypresupuesto.delete_from_db()
        flash('Exito: Se ha eliminado correctamente el presupuesto')
        return redirect(url_for('presupuestos.html'))
    flash('Error: No se ha conseguido eliminar el presupuesto')
    return render_template('presupuestoInfo.html',mytitle='Info Presupuesto', mypresupuesto=mypresupuesto)



@presupuestos.route("/presupuestos/nuevo", methods=['POST'])
def nuevo():
    r = request.form
    fecha = datetime.date.today()

    mypresupuesto=PresupuestosModel(r['nombre'],r['telefono'],r['email'],fecha,r['modelo'],r['maderaCuerpo'],
                                    r['maderaDiapason'],r['maderaMastil'],r['mastil'],r['pastillaMastil'],
                                    r['pastillaMedio'],'pastillaPuente','puente',r['tono1'],r['tono2'],
                                    r['volumen'],r['tapa'],r['chapa'],r['jack'],r['acabado'],
                                    r['colorCuerpo'], r['colorGolpeador'],
                                    r['colorPastillaMastil'], r['colorPastillaMedio'], 'colorPastillaPuente',
                                    'colorPuente',r['colorTono1'],r['colorTono2'],
                                    r['colorVolumen'],r['colorTapa'],r['colorChapa'],r['colorJack'],r['comentarios'])

    mypresupuesto.insert_to_db()
    flash('Exito: Nos pondremos en contacto contigo, para valorar el presupuesto')
    return redirect(url_for('index'))