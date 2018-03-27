from flask import Blueprint,render_template, request, redirect, url_for
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
    producto = ArtistasModel.query.filter_by(nombre=nombre).first()
    producto.nombre=request.form['nombre']
    producto.descripcion=request.form['descrip']
    if request.form['myfoto'] is not '':
        producto.fotopal=request.form['myfoto']
    producto.actualizar()
    id = ArtistasModel.find_by_name(nombre).id
    fotos = int((len(request.form)-2)/2)
    for index in range(1, fotos+1):
        mifoto = FotosArtistasModel(request.form['alt' + index.__str__()],request.form['myfoto' + index.__str__()],id)
        mifoto.insert_to_db()

    return redirect(url_for('infoartista.html', nombre=nombre))