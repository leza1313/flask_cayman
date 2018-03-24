from flask import Blueprint,render_template, request, redirect, url_for
from flask_login import login_required
from flask import current_app as app
from flask import request

from models.artistas import ArtistasModel

infoartista = Blueprint('infoartista', __name__)

@infoartista.route('/infoartista/<string:name>')
def html(name):
    artista = ArtistasModel.query.filter_by(nombre=name).first()
    return render_template('infoartista.html', myartista=artista, mytitle='Info Artista')

@infoartista.route('/editarartista/<string:nombre>', methods=['POST'])
@login_required
def editar(nombre):
    artista = ArtistasModel.query.filter_by(nombre=nombre).first()
    artista.nombre=request.form['nombre']
    artista.descripcion=request.form['descrip']
    artista.foto1=request.form['fot']
    artista.actualizar()
    return redirect(url_for('infoartista.html', name=artista.nombre))