from flask import Blueprint,render_template
from flask import current_app as app
from flask import request

from models.artistas import ArtistasModel

infoartista = Blueprint('infoartista', __name__)

@infoartista.route('/infoartista')
def html():
    if request.args.get('artista') is not None:
        myartista = request.args.get('artista')
        artista = ArtistasModel.query.filter_by(nombre=myartista).first()
    return render_template('infoartista.html', myartista=artista)
