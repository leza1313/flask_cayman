from flask import Blueprint,render_template, redirect, url_for, flash
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
        producto.acabado = request.form['acabado']
        producto.pastillas = request.form['pastillas']
        producto.puente = request.form['puente']
        producto.electronica = request.form['electronica']
        producto.clavijero = request.form['clavijero']
        if request.form['myfoto'].__str__() is not '':
            producto.fotopal=request.form['myfoto']
        producto.actualizar()
        if 'alt1' not in request.args:
            flash('Exito: Se ha actualizado el bajo correctamente')
            return redirect(url_for('infoproducto.html', tipo='bajo', nombre=producto.nombre))
        id = BajosModel.find_by_name(nombre).id
        fotos = int((len(request.form)-2)/2)
        for index in range(1, fotos+1):
            if request.form['myfoto'+index.__str__()] is '':
                flash('Error: Es necesario seleccionar una imagen')
                return redirect(url_for('infoproducto.html', tipo=tipo, nombre=nombre))
            mifoto = FotosBajosModel(request.form['alt' + index.__str__()],request.form['myfoto' + index.__str__()],id)
            mifoto.insert_to_db()
        flash('Exito: Se ha actualizado el bajo correctamente')
        return redirect(url_for('infoproducto.html', tipo='bajo', nombre=producto.nombre))
    if tipo =='guitarra':
        producto = GuitarrasModel.query.filter_by(nombre=nombre).first()
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descrip']
        producto.acabado = request.form['acabado']
        producto.pastillas = request.form['pastillas']
        producto.puente = request.form['puente']
        producto.electronica = request.form['electronica']
        producto.clavijero = request.form['clavijero']
        if request.form['myfoto'].__str__() is not '':
            producto.fotopal=request.form['myfoto']
        producto.actualizar()
        if 'alt1' not in request.args:
            flash('Exito: Se ha actualizado la guitarra correctamente')
            return redirect(url_for('infoproducto.html', tipo='guitarra', nombre=producto.nombre))
        id = GuitarrasModel.find_by_name(nombre).id
        fotos = int((len(request.form)-2)/2)
        for index in range(1, fotos+1):
            if request.form['myfoto'+index.__str__()] is '':
                flash('Error: Es necesario seleccionar una imagen')
                return redirect(url_for('infoproducto.html', tipo=tipo, nombre=nombre))
            mifoto = FotosGuitarrasModel(request.form['alt' + index.__str__()],request.form['myfoto' + index.__str__()],id)
            mifoto.insert_to_db()

        flash('Exito: Se ha actualizado la guitarra correctamente')
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
        flash('Exito: Se ha borrado la foto del articulo correctamente')
    return redirect(url_for('infoproducto.html', tipo=tipo, nombre=nombre))



