from flask import Blueprint,render_template
from flask import current_app as app

from models.bajos import BajosModel

bajos = Blueprint('bajos', __name__)

@bajos.route('/bajos')
def html():
    misbajos=BajosModel.query.all()
    return render_template('bajos.html', bajos=misbajos)
