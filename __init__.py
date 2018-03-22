import sys
sys.path.append('/var/www/flask_cayman/flask_cayman')


from flask import Flask
from flask import render_template
from flask_restful import Api

from connection import db

from pages import editor
from pages import guitarras
from pages import bajos
from pages import infoproducto
from pages import galeria
from pages import artistas
from pages import infoartista

from resources.guitarras import Guitarras, GuitarrasList
from resources.bajos import Bajos, BajosList

app = Flask(__name__)
app.debug = True

app.config.from_object('config.ProductionConfig')

db.init_app(app)

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

app.register_blueprint(guitarras.guitarras)

app.register_blueprint(infoproducto.infoproducto)

app.register_blueprint(bajos.bajos)

app.register_blueprint(galeria.galeria)

app.register_blueprint(artistas.artistas)

app.register_blueprint(infoartista.infoartista)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run()
