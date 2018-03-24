from flask import Blueprint,render_template, redirect, url_for, request
from flask_login import login_required
from flask import current_app as app

from models.artistas import ArtistasModel

artistas = Blueprint('artistas', __name__)

@artistas.route('/artistas')
def html():
    myartistas=ArtistasModel.query.all()
    return render_template('artistas.html', myartistas=myartistas, mytitle='Artistas')


@artistas.route('/borrarartista/<string:nombre>')
@login_required
def borrar(nombre):
    miartista = ArtistasModel.find_by_name(nombre)
    if miartista:
        miartista.delete_from_db()
    return redirect(url_for('artistas.html'))

@artistas.route('/nuevoartista', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        foto = request.form['foto']

        miartista = ArtistasModel(nombre,foto,foto,foto,foto,descripcion)
        #print(mibajo)
        miartista.insert_to_db()

    return render_template('nuevoartista.html', mytitle='Añadir Artista')
