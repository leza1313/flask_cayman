import sys
sys.path.append('/var/www/flask_cayman/flask_cayman')


from flask import Flask
from flask import render_template
from pages import editor
from flask_sqlalchemy import SQLAlchemy

from models import guitarras


app = Flask(__name__)
app.debug = True

app.config.from_object('config.ProductionConfig')

"""mysql = MySQL()
mysql.init_app(app)
cursor = mysql.connect().cursor()
"""

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

@app.route('/guitarras1')
def guitarras1():
    misguitarras=guitarras.query.all()
    return render_template('guitarras1.html', guitarras=misguitarras)


@app.route('/bajos')
def bajos():
    pass

@app.route('/contacto')
def contacto():
    pass
if __name__ == '__main__':
    app.run()
