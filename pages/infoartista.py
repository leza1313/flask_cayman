from flask import Blueprint,render_template
from flask import current_app as app
from flask import request

from models.artistas import ArtistasModel

infoartista = Blueprint('infoartista', __name__)

@infoartista.route('/infoartista/<string:name>')
def html(name):
    artista = ArtistasModel.query.filter_by(nombre=name).first()
    return render_template('infoartista.html', myartista=artista, mytitle='Info Artista')
