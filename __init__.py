import sys
sys.path.append('/var/www/flask_cayman/flask_cayman')


from flask import Flask
from flask import render_template
from pages import editor
from flaskext.mysql import MySQL



app = Flask(__name__)
app.debug = True

app.config.from_object('config.ProductionConfig')

mysql = MySQL()

mysql.init_app(app)

@app.route('/')
def index():
    title='Inicio'
    return render_template('index.html', mytitle=title)

app.register_blueprint(editor.editor)


@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/guitarras')
def guitarras():
    pass

@app.route('/bajos')
def bajos():
    pass

@app.route('/contacto')
def contacto():
    pass
if __name__ == '__main__':
    app.run()
