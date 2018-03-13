import sys
sys.path.append('/var/www/flask_cayman/flask_cayman')


from flask import Flask
from flask import render_template
from pages import editor
from flask_sqlalchemy import SQLAlchemy
from flask import request

from models import Guitarras
from models import Bajos



app = Flask(__name__)
app.debug = True

app.config.from_object('config.ProductionConfig')

db=SQLAlchemy(app)


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
def guitarras():
    misguitarras=Guitarras.query.all()
    return render_template('guitarras.html', guitarras=misguitarras)

@app.route('/infoproducto')
def infoproducto():
    if request.args.get('bajo') is not None:
        bajo = request.args.get('bajo')
        producto = Bajos.query.filter_by(nombre=bajo).first()
    if request.args.get('guitarra') is not None:
        guitarra = request.args.get('guitarra')
        producto = Guitarras.query.filter_by(nombre=guitarra).first()
    return render_template('infoproducto.html', miproducto=producto)

@app.route('/bajos')
def bajos():
    misbajos=Bajos.query.all()
    return render_template('bajos.html', bajos=misbajos)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run()
