import sys
sys.path.append('/var/www/flask_cayman/flask_cayman')


from flask import Flask
from flask import render_template
from pages import editor
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask_restful import Api
from flask_resize import Resize

from resources.guitarras import Guitarras, GuitarrasList
from resources.bajos import Bajos, BajosList
from models.guitarras import GuitarrasModel
from models.bajos import BajosModel

import os


app = Flask(__name__)
app.debug = True


app.config['RESIZE_URL'] = 'static/img'
app.config['RESIZE_ROOT'] = os.path.join(app.root_path,'static/img')

resize = Resize(app)


app.config.from_object('config.ProductionConfig')

db=SQLAlchemy(app)
api = Api(app)

##Anade en esos endpoints los recursos a mostrar
api.add_resource(Guitarras, '/api/guitarra/<string:name>')
api.add_resource(GuitarrasList, '/api/guitarras/')
api.add_resource(Bajos, '/api/bajo/<string:name>')
api.add_resource(BajosList, '/api/bajos/')

@app.route('/')
def index():
    title='Inicio'
    return render_template('index.html', mytitle=title)

app.register_blueprint(editor.editor)

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/guitarras')
def guitarras_page():
    misguitarras = GuitarrasModel.query.all()
    return render_template('guitarras.html', guitarras=misguitarras)

@app.route('/infoproducto')
def infoproducto():
    if request.args.get('bajo') is not None:
        bajo = request.args.get('bajo')
        producto = BajosModel.query.filter_by(nombre=bajo).first()
    if request.args.get('guitarra') is not None:
        guitarra = request.args.get('guitarra')
        producto = GuitarrasModel.query.filter_by(nombre=guitarra).first()
    return render_template('infoproducto.html', miproducto=producto)

@app.route('/bajos')
def bajos_page():
    misbajos=BajosModel.query.all()
    return render_template('bajos.html', bajos=misbajos)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run()
