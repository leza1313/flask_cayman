from flask import Blueprint,render_template, redirect, url_for, request,flash
from flask_login import login_required
from flask import current_app as app

from models.artistas import ArtistasModel
from models.fotosartistas import FotosArtistasModel

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
        flash('Exito: Se ha eliminado correctamente el artista')
        return redirect(url_for('artistas.html'))
    flash('Error: No se ha conseguido eliminar el artista')
    return redirect(url_for('artistas.html'))

@artistas.route('/nuevoartista', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descrip']
        foto = request.form['myfoto']
        if foto.__str__() is '':
            flash('Error: Es necesario seleccionar una imagen')
            return redirect(url_for('artistas.nuevo'))

        miartista = ArtistasModel(nombre, descripcion, foto)
        miartista.insert_to_db()
        id = ArtistasModel.find_by_name(nombre).id
        fotos = int((len(request.form) - 3) / 2)

        for index in range(1, fotos+1):
            mifoto = FotosArtistasModel(request.form['alt'+index.__str__()],request.form['myfoto'+index.__str__()], id)
            mifoto.insert_to_db()
        flash('Exito: Se ha anadido correctamente el nuevo artista')
        return redirect(url_for('artistas.html'))
    return render_template('nuevoartista.html', mytitle='Anadir Artista')
