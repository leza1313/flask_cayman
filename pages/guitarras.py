from flask import Blueprint,render_template
from flask import current_app as app

from models.guitarras import GuitarrasModel

guitarras = Blueprint('guitarras', __name__)



@guitarras.route('/guitarras')
def html():
    misguitarras = GuitarrasModel.query.all()
    return render_template('guitarras.html', guitarras=misguitarras)
