from flask import Blueprint,render_template
from flask import current_app as app

from models.artistas import ArtistasModel

artistas = Blueprint('artistas', __name__)

@artistas.route('/artistas')
def html():
    myartistas=ArtistasModel.query.all()
    return render_template('artistas.html', myartistas=myartistas)
