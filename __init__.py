import sys

import os

sys.path.append('/var/www/flask_cayman/flask_cayman')


from flask import Flask, send_from_directory
from flask import render_template, redirect, url_for, flash, request
from flask_restful import Api
from flask_login import LoginManager, login_required, logout_user
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

from connection import db
from models.user import UserModel
from models.fotosbajos import FotosBajosModel
from models.fotosguitarras import FotosGuitarrasModel
from models.promociones import PromocionesModel
from models.editor import ModelosModel, Partes3DModel, Opciones3DModel, Precios3DModel
from models.presupuestos import PresupuestosModel

from pages import editor
from pages import guitarras
from pages import bajos
from pages import infoproducto
from pages import galeria
from pages import artistas
from pages import infoartista
from pages import login
from pages import promociones
from pages import pedidos
from pages import presupuestos

import paypal_ipn

from resources.guitarras import Guitarras, GuitarrasList
from resources.bajos import Bajos, BajosList
from resources.artistas import Artistas, ArtistasList
from resources.pedidos import Pedidos, PedidosList, TopModelo, CountEsteMes
from resources.editor import Partes3D, Opciones3D, TodasOpciones3D, Precio3D, TodosPrecio3D, Parte3D

app = Flask(__name__)
app.debug = True

app.config.from_object('config.ProductionConfig')
app.config['UPLOAD_FOLDER']=os.path.dirname(os.path.abspath(__file__))+'/static'
db.init_app(app)
@app.before_first_request
def create_db():
    db.create_all()
    db.session.commit()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login.html'

@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))

api = Api(app)

jwt = JWT(app, authenticate, identity)

##Anade en esos endpoints los recursos a mostrar
api.add_resource(Guitarras, '/api/guitarra/<string:name>')
api.add_resource(GuitarrasList, '/api/guitarras/')
api.add_resource(Bajos, '/api/bajo/<string:name>')
api.add_resource(BajosList, '/api/bajos/')
api.add_resource(Artistas, '/api/artista/<string:name>')
api.add_resource(ArtistasList, '/api/artistas/')
api.add_resource(Pedidos, '/api/pedido/<string:num>')
api.add_resource(PedidosList, '/api/pedidos/')
api.add_resource(TopModelo, '/api/top/modelo/')
api.add_resource(CountEsteMes, '/api/countestemes/')
api.add_resource(Partes3D, '/api/partes3D/')
api.add_resource(Parte3D, '/api/parte3D/<string:parte3D>')
api.add_resource(Opciones3D, '/api/opciones3D/<string:parte3D>')
api.add_resource(TodasOpciones3D, '/api/todasOpciones3D/')
api.add_resource(Precio3D, '/api/precio3D/<string:parte3D>/<string:material>/')
api.add_resource(TodosPrecio3D, '/api/todosPrecio3D/<string:parte3D>')



app.register_blueprint(login.login)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))

import logging
from logging.handlers import RotatingFileHandler

formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - \n%(message)s\n-------------------------\n")
handler = RotatingFileHandler('/var/prueba/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
app.logger.addHandler(handler)


@app.route('/log')
def prueba1():
    headers = request.headers
    params = request.json
    app.logger.warning("{}{}".format(headers,params))
    return ('Peticion recibida')


@app.route('/')
def index():
    mispromociones=PromocionesModel.query.all()
    return render_template('index.html', mytitle='Inicio', mispromociones=mispromociones)

app.register_blueprint(editor.editor)

app.register_blueprint(promociones.promociones)

@app.route('/prueba')
def prueba():
    #aa = Partes3DModel('Standard2', 'Cuerpo', 'Stratocaster', 10, 10, 10, 'static/modelos/prueba/strat cuerpo.json',
    #              'rojo.jpg')
    #aa.insert_to_db()
    #bb = Opciones3DModel('strato2opcion1','static/modelos/prueba/sunburst.jpg','firebird.png',2)
    #bb.insert_to_db()
    return render_template('prueba.html')

@app.route('/pagocancelado')
def pagocancelado():
    return render_template('errorpago.html')

@app.route('/pagocorrecto')
def pagocorrecto():
    return render_template('pagocorrecto.html')




@app.route('/productos')
def productos():
    return render_template('productos.html', mytitle='Productos')

app.register_blueprint(guitarras.guitarras)

app.register_blueprint(infoproducto.infoproducto)

app.register_blueprint(bajos.bajos)

app.register_blueprint(galeria.galeria)

app.register_blueprint(artistas.artistas)

app.register_blueprint(infoartista.infoartista)

##PAYPAL_IPN
app.register_blueprint(paypal_ipn.paypal_ipn)

app.register_blueprint(pedidos.pedidos)

app.register_blueprint(presupuestos.presupuestos)


@app.route('/contacto')
def contacto():
    return render_template('contacto.html',mytitle='Contacto')

@app.route('/android', methods=['GET'])
@login_required
def download():
    uploads = os.path.join(app.root_path, "app")
    print(uploads)
    return send_from_directory(uploads, "app-debug.apk")

if __name__ == '__main__':
    app.run()
