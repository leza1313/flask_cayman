from flask import Flask
from flask import render_template

import sys
sys.path.append('pages/')

from pages import editor

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    title='Inicio'
    return render_template('index.html', mytitle=title)

app.register_blueprint(editor.editor)


@app.route('/productos')
def productos():
    return render_template('prueba.html')

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
