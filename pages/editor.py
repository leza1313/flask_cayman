from flask import Blueprint,render_template
from flask import current_app as app
editor = Blueprint('editor', __name__)

from models.editor import Partes3DModel,Opciones3DModel,Precios3DModel

class myModal:
    def __init__(self, id, titulo,opcionesModelo,opcionesColor):
        self.id = id
        self.titulo = titulo
        self.opcionesModelo=opcionesModelo
        self.opcionesColor=opcionesColor
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
    Asi simplifico el codigo reutilizandolo, y permitiendo al administrador que gestione 
    el editor 3D
    """
    #opcionesCuerpo, es un array con las opciones que tiene esa pieza en concreto
    opcionesCuerpo=[]
    opcionesGolpeador=[]
    opcionesMastil=[]
    opcionesPastillaMastil=[]
    opcionesPastillaMedio=[]
    opcionesPastillaPuente=[]
    opcionesPuente=[]
    opcionesTono1=[]
    opcionesTono2=[]
    opcionesVolumen=[]
    opcionesClavijero=[]
    opcionesDiapason=[]


    #cuerpos, es un array con todos los cuerpos disponibles
    cuerpos=Partes3DModel.find_by_pieza('Cuerpo')
    golpeadores=Partes3DModel.find_by_pieza('Golpeador')
    mastiles=Partes3DModel.find_by_pieza('Mastil')
    pastillasMastil=Partes3DModel.find_by_pieza('PastillaMastil')
    pastillasMedio=Partes3DModel.find_by_pieza('PastillaMedio')
    pastillasPuente=Partes3DModel.find_by_pieza('PastillaPuente')
    puentes=Partes3DModel.find_by_pieza('Puente')
    tonos1=Partes3DModel.find_by_pieza('Tono1')
    tonos2=Partes3DModel.find_by_pieza('Tono2')
    volumenes=Partes3DModel.find_by_pieza('Volumen')
    clavijeros=Partes3DModel.find_by_pieza('Clavijero')
    diapasones=Partes3DModel.find_by_pieza('Diapason')

    opcionesModelo1=[]
    for index, item in enumerate(cuerpos):
        opcionesCuerpo.append(Opciones3DModel.find_by_parte(item.id))
        aux=myOpciones(item.rutaJSON,item.foto)
        opcionesModelo1.append(aux)
    #print(opcionesModelo1[0].modelo)

    opcionesGolpeador1 = []
    for index, item in enumerate(golpeadores):
        opcionesGolpeador.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesGolpeador1.append(aux)

    opcionesMastil1=[]
    for index, item in enumerate(mastiles):
        opcionesMastil.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesMastil1.append(aux)

    for index, item in enumerate(pastillasMastil):
        opcionesPastillaMastil.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(pastillasMedio):
        opcionesPastillaMedio.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(pastillasPuente):
        opcionesPastillaPuente.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(puentes):
        opcionesPuente.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(tonos1):
        opcionesTono1.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(tonos2):
        opcionesTono2.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(volumenes):
        opcionesVolumen.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(clavijeros):
        opcionesClavijero.append(Opciones3DModel.find_by_parte(item.id))

    for index, item in enumerate(diapasones):
        opcionesDiapason.append(Opciones3DModel.find_by_parte(item.id))

    listaCuerpos=[]
    for index, item in enumerate(cuerpos):
        listaCuerpos.append(myModal('modalCuerpo'+index.__str__(),'Escoge Modelo', opcionesModelo1,opcionesCuerpo[index]))
    #print(listaCuerpos[0].opcionesModelo[1].modelo)
    print(opcionesCuerpo[0][0].rutaTextura)
    #cuerpoStrato2 = myModal('modalCuerpoStrato2','Escoge Modelo',cuerpos,opcionesCuerpo[1])

    listaGolpeadores = []
    for index, item in enumerate(golpeadores):
        listaGolpeadores.append(
            myModal('modalGolpeador' + index.__str__(), 'Escoge Golpeador', opcionesGolpeador1, opcionesGolpeador[index]))

    listaMastiles = []
    for index, item in enumerate(golpeadores):
        listaMastiles.append(
            myModal('modalMastil' + index.__str__(), 'Escoge Mastil', opcionesMastil1,
                    opcionesMastil[index]))

    """golpeador = myModal('modalGolpeador','Escoge Golpeador','','')

    mastil = myModal('modalMastil','Escoge Mastil','','')

    pastilla_mastil = myModal('modalPastilla_Mastil','Escoge Pastilla Mastil','','')

    pastilla_medio = myModal('modalPastilla_Medio','Escoge Pastilla Medio','','')

    pastilla_puente = myModal('modalPastilla_Puente','Escoge Pastilla Puente','','')

    puente = myModal('modalPuente','Escoge Puente','','')

    per_tono = myModal('modalTono_1','Escoge Perilla tono 1','','')

    per_tono2 = myModal('modalTono_2','Escoge Perilla tono 2','','')

    per_volumen = myModal('modalVolumen','Escoge Perilla volumen','','')"""


    lista = [
        listaCuerpos,
        listaGolpeadores,
        listaMastiles
    ]
    return render_template('loader.html', mytitle=title, lista=lista)
