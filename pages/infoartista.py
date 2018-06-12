from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required
from flask import current_app as app
from flask import request

from models.artistas import ArtistasModel
from models.fotosartistas import FotosArtistasModel

infoartista = Blueprint('infoartista', __name__)

@infoartista.route('/infoartista/<string:name>')
def html(name):
    artista = ArtistasModel.query.filter_by(nombre=name).first()
    return render_template('infoartista.html', myartista=artista, mytitle='Info Artista')

@infoartista.route('/editarartista/<string:nombre>', methods=['POST'])
@login_required
def editar(nombre):
    print(request.form)
    producto = ArtistasModel.query.filter_by(nombre=nombre).first()
    producto.nombre=request.form['nombre']
    producto.descripcion=request.form['descrip']
    if request.form['myfoto'].__str__() is not '':
        producto.fotopal=request.form['myfoto']
    producto.actualizar()
    if 'alt1' not in request.form:
        flash('Exito: Se ha actualizado el artista correctamente')
        return redirect(url_for('infoartista.html',name=producto.nombre))
    id = ArtistasModel.find_by_name(nombre).id
    fotos = int((len(request.form)-2)/2)
    for index in range(1, fotos):
        print(index)
        mifoto = FotosArtistasModel(request.form['alt' + index.__str__()],request.form['myfoto' + index.__str__()],id)
        mifoto.insert_to_db()
    flash('Exito: Se ha actualizado el artista correctamente')
    return redirect(url_for('infoartista.html', name=producto.nombre))

@infoartista.route('/borrarinfoartistafoto/<string:nombre>/<string:id>/<string:crop2>/<string:crop3>')
@login_required
def borrar(nombre, id,crop2,crop3):
    url = 'https://ucarecdn.com/' + id + '/-/crop/' + crop2 + '/' + crop3 + '/-/preview/'
    mifoto = FotosArtistasModel.find_by_name(url)
    if mifoto:
        mifoto.delete_from_db()
        flash('Exito: Se ha borrado la foto del artista correctamente')
    return redirect(url_for('infoartista.html', name=nombre))
