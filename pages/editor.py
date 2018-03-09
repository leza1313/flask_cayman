from flask import Blueprint,render_template
from flask import current_app as app
editor = Blueprint('editor', __name__)


class myModal:
    def __init__(self, id, titulo,opciones):
        self.id = id
        self.titulo = titulo
        self.opciones=opciones
class myOpciones:
    def __init__(self,modelo,foto):
        self.modelo=modelo
        self.foto=foto

@editor.route("/editor")
def html():
    title = 'Taller Custom'

    """
    Si guardo todo esto en una BBDD (MySql), con hacer CRUD a esas tablas
    consigo que el administrador pueda gestionar este editor.
    Anadiendo mas modelos STL de diferentes cuerpos de guitarras,
    anadiendo mas texturas y tambien modificando el menu derecho del editor

    Mirar el JS editor.js, para ver si se pueden cargar todos los modelos de un array.
    Asi simplifico el código reutilizandolo, y permitiendo al administrador que gestione 
    el editor 3D
    """
    opcionCuerpo1 = myOpciones('tele2.STL','firebird.png')
    opcionCuerpo2 = myOpciones('CUERPO.STL','strato.png')
    opcionesCuerpo = [opcionCuerpo1,opcionCuerpo2]
    cuerpo = myModal('modalModelo','Escoge Modelo',opcionesCuerpo)

    golpeador = myModal('modalGolpeador','Escoge Golpeador','')

    mastil = myModal('modalMastil','Escoge Mastil','')

    pastilla_mastil = myModal('modalPastilla_Mastil','Escoge Pastilla Mastil','')


    lista = [
        cuerpo,
        golpeador,
        mastil,
        pastilla_mastil
    ]
    return render_template('loader.html', mytitle=title, lista=lista)