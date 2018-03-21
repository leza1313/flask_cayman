from flask import Blueprint,render_template
from models.galeria import GaleriaModel


galeria = Blueprint('galeria', __name__)

@galeria.route('/galeria')
def html():
    mygaleria = GaleriaModel.query.all()
    return render_template('galeria.html', mygaleria=mygaleria)
