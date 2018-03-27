from flask import Blueprint,render_template, redirect, url_for
from flask_login import login_required
from flask import current_app as app
from flask import request

from models.guitarras import GuitarrasModel
from models.bajos import BajosModel
from models.fotosbajos import FotosBajosModel
from models.fotosguitarras import FotosGuitarrasModel

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
        if request.form['myfoto'] is not '':
            producto.fotopal=request.form['myfoto']
        producto.actualizar()
        id = BajosModel.find_by_name(nombre).id
        fotos = int((len(request.form)-2)/2)
        for index in range(1, fotos+1):
            mifoto = FotosBajosModel(request.form['alt' + index.__str__()],request.form['myfoto' + index.__str__()],id)
            mifoto.insert_to_db()
        return redirect(url_for('infoproducto.html', tipo='bajo', nombre=producto.nombre))
    if tipo =='guitarra':
        producto = GuitarrasModel.query.filter_by(nombre=nombre).first()
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descrip']
        if request.form['myfoto'] is not '':
            producto.fotopal=request.form['myfoto']
        id = GuitarrasModel.find_by_name(nombre).id
        fotos = int((len(request.form)-2)/2)
        for index in range(1, fotos+1):
            mifoto = FotosGuitarrasModel(request.form['alt' + index.__str__()],request.form['myfoto' + index.__str__()],id)
            mifoto.insert_to_db()
        producto.actualizar()
        return redirect(url_for('infoproducto.html', tipo='guitarra', nombre=producto.nombre))
    return redirect(url_for('infoproducto.html', tipo=tipo, nombre=nombre))

@infoproducto.route('/borrarinfoproductofoto/<string:tipo>/<string:nombre>/<string:id>')
@login_required
def borrar(tipo, nombre, id):
    url = 'https://ucarecdn.com/'+id+'/'
    if tipo=='bajo':
        mifoto = FotosBajosModel.find_by_name(url)
    if tipo=='guitarra':
        mifoto = FotosGuitarrasModel.find_by_name(url)
    if mifoto:
        mifoto.delete_from_db()
    return redirect(url_for('infoproducto.html', tipo=tipo, nombre=nombre))



