from flask import Blueprint,render_template, redirect, url_for
from flask_login import login_required
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
    return render_template('infoproducto.html', miproducto=producto, mytitle='Info Producto')

@infoproducto.route('/editarproducto/<string:tipo>/<string:nombre>', methods=['POST'])
@login_required
def editar(tipo,nombre):
    if tipo=='bajo':
        producto = BajosModel.query.filter_by(nombre=nombre).first()
        producto.nombre=request.form['nombre']
        producto.descripcion=request.form['descrip']
        producto.foto1=request.form['fot']
        producto.actualizar()
        return redirect(url_for('infoproducto.html', tipo='bajo', nombre=producto.nombre))
    if tipo =='guitarra':
        producto = GuitarrasModel.query.filter_by(nombre=nombre).first()
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descrip']
        producto.foto1 = request.form['fot']
        producto.actualizar()
        return redirect(url_for('infoproducto.html', tipo='guitarra', nombre=producto.nombre))
    return redirect(url_for('infoproducto.html', tipo=tipo, nombre=nombre))



