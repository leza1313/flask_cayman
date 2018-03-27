import sys
sys.path.append('/var/www/flask_cayman/flask_cayman')


from flask import Flask
from flask import render_template, redirect, url_for, flash
from flask_restful import Api
from flask_login import LoginManager, login_required, logout_user

from connection import db
from models.user import UserModel
from models.fotosbajos import FotosBajosModel
from models.fotosguitarras import FotosGuitarrasModel
from models.promociones import PromocionesModel

from pages import editor
from pages import guitarras
from pages import bajos
from pages import infoproducto
from pages import galeria
from pages import artistas
from pages import infoartista
from pages import login
from pages import promociones

from resources.guitarras import Guitarras, GuitarrasList
from resources.bajos import Bajos, BajosList

app = Flask(__name__)
app.debug = True

app.config.from_object('config.ProductionConfig')

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

##Anade en esos endpoints los recursos a mostrar
api.add_resource(Guitarras, '/api/guitarra/<string:name>')
api.add_resource(GuitarrasList, '/api/guitarras/')
api.add_resource(Bajos, '/api/bajo/<string:name>')
api.add_resource(BajosList, '/api/bajos/')


app.register_blueprint(login.login)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.html'))

@app.route('/')
def index():
    mispromociones=PromocionesModel.query.all()
    return render_template('index.html', mytitle='Inicio', mispromociones=mispromociones)

app.register_blueprint(editor.editor)

app.register_blueprint(promociones.promociones)

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/productos')
def productos():
    return render_template('productos.html', mytitle='Productos')

app.register_blueprint(guitarras.guitarras)

app.register_blueprint(infoproducto.infoproducto)

app.register_blueprint(bajos.bajos)

app.register_blueprint(galeria.galeria)

app.register_blueprint(artistas.artistas)

app.register_blueprint(infoartista.infoartista)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html',mytitle='Contacto')

if __name__ == '__main__':
    app.run()
