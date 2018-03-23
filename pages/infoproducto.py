from flask import Blueprint,render_template
from flask import current_app as app
from flask import request

from models.guitarras import GuitarrasModel
from models.bajos import BajosModel

infoproducto = Blueprint('infoproducto', __name__)

@infoproducto.route('/infoproducto/<string:tipo>/<string:nombre>')
def html(tipo,nombre):
    if tipo=='bajo':
        producto = BajosModel.query.filter_by(nombre=nombre).first()
    if tipo =='guitarra':
        producto = GuitarrasModel.query.filter_by(nombre=nombre).first()
    return render_template('infoproducto.html', miproducto=producto)
