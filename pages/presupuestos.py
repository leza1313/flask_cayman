from flask import Blueprint,render_template,redirect,url_for,request
from flask import current_app as app
presupuestos = Blueprint('presupuestos', __name__)

from models.presupuestos import PresupuestosModel

import datetime


@presupuestos.route("/presupuestos", methods=['GET'])
def html():
    mypresupuestos= PresupuestosModel.query.all()
    return render_template('presupuestos.html',mytitle='Presupuestos', mypresupuestos=mypresupuestos)

@presupuestos.route("/presupuestos/nuevo", methods=['POST'])
def nuevo():
    r = request.form
    print(r)
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
    return redirect(url_for('index'))