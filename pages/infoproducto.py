from flask import Blueprint,render_template
from flask import current_app as app
from flask import request

from models.guitarras import GuitarrasModel
from models.bajos import BajosModel

infoproducto = Blueprint('infoproducto', __name__)

@infoproducto.route('/infoproducto')
def html():
    if request.args.get('bajo') is not None:
        bajo = request.args.get('bajo')
        producto = BajosModel.query.filter_by(nombre=bajo).first()
    if request.args.get('guitarra') is not None:
        guitarra = request.args.get('guitarra')
        producto = GuitarrasModel.query.filter_by(nombre=guitarra).first()
    return render_template('infoproducto.html', miproducto=producto)
