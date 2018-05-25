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
    #opcionesClavijero=[]
    opcionesDiapason=[]
    opcionesTapa=[]
    opcionesChapa=[]
    opcionesJack=[]


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
    #clavijeros=Partes3DModel.find_by_pieza('Clavijero')
    diapasones=Partes3DModel.find_by_pieza('Diapason')
    tapas=Partes3DModel.find_by_pieza('Tapa')
    chapas=Partes3DModel.find_by_pieza('Chapa')
    jacks=Partes3DModel.find_by_pieza('Jack')

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

    opcionesPastillaMastil1=[]
    for index, item in enumerate(pastillasMastil):
        opcionesPastillaMastil.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesPastillaMastil1.append(aux)

    opcionesPastillaMedio1 = []
    for index, item in enumerate(pastillasMedio):
        opcionesPastillaMedio.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesPastillaMedio1.append(aux)

    opcionesPastillaPuente1=[]
    for index, item in enumerate(pastillasPuente):
        opcionesPastillaPuente.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesPastillaPuente1.append(aux)

    opcionesPuente1 = []
    for index, item in enumerate(puentes):
        opcionesPuente.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesPuente1.append(aux)

    opcionesTono11 = []
    for index, item in enumerate(tonos1):
        opcionesTono1.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesTono11.append(aux)

    opcionesTono21 = []
    for index, item in enumerate(tonos2):
        opcionesTono2.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesTono21.append(aux)

    opcionesVolumen1 = []
    for index, item in enumerate(volumenes):
        opcionesVolumen.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesVolumen1.append(aux)

    ##QUE ONDA CON CLAVIJERO Y PUENTE
    #for index, item in enumerate(clavijeros):
        #opcionesClavijero.append(Opciones3DModel.find_by_parte(item.id))

    opcionesDiapason1 = []
    for index, item in enumerate(diapasones):
        opcionesDiapason.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesDiapason1.append(aux)

    opcionesTapa1 = []
    for index, item in enumerate(tapas):
        opcionesTapa.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesTapa1.append(aux)

    opcionesChapa1 = []
    for index, item in enumerate(chapas):
        opcionesChapa.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesChapa1.append(aux)

    opcionesJack1 = []
    for index, item in enumerate(jacks):
        opcionesJack.append(Opciones3DModel.find_by_parte(item.id))
        aux = myOpciones(item.rutaJSON, item.foto)
        opcionesJack1.append(aux)

    ########################################
    ##LISTA DE LOS MODELOS CON SUS OPCIONES#
    ########################################

    listaCuerpos=[]
    for index, item in enumerate(cuerpos):
        listaCuerpos.append(myModal('modalCuerpo'+index.__str__(),'Escoge Modelo', opcionesModelo1,opcionesCuerpo[index]))
    #print(listaCuerpos[0].opcionesModelo[1].modelo)
    #print(opcionesCuerpo[0][0].rutaTextura)
    #cuerpoStrato2 = myModal('modalCuerpoStrato2','Escoge Modelo',cuerpos,opcionesCuerpo[1])

    listaGolpeadores = []
    for index, item in enumerate(golpeadores):
        listaGolpeadores.append(
            myModal('modalGolpeador' + index.__str__(), 'Escoge Golpeador', opcionesGolpeador1, opcionesGolpeador[index]))

    listaMastiles = []
    for index, item in enumerate(mastiles):
        listaMastiles.append(
            myModal('modalMastil' + index.__str__(), 'Escoge Mastil', opcionesMastil1,
                    opcionesMastil[index]))

    listaDiapasones = []
    for index, item in enumerate(diapasones):
        listaDiapasones.append(
            myModal('modalDiapason' + index.__str__(), 'Escoge Diapason', opcionesDiapason1,
                    opcionesDiapason[index]))

    listaPastillasMastil = []
    for index, item in enumerate(pastillasMastil):
        listaPastillasMastil.append(
            myModal('modalPastillaMastil' + index.__str__(), 'Escoge Pastilla Mastil', opcionesPastillaMastil1,
                    opcionesPastillaMastil[index]))

    listaPastillasMedio = []
    for index, item in enumerate(pastillasMedio):
        listaPastillasMedio.append(
            myModal('modalPastillaMedio' + index.__str__(), 'Escoge Pastilla Medio', opcionesPastillaMedio1,
                    opcionesPastillaMedio[index]))

    listaPastillasPuente = []
    for index, item in enumerate(pastillasMedio):
        listaPastillasPuente.append(
            myModal('modalPastillaPuente' + index.__str__(), 'Escoge Pastilla Puente', opcionesPastillaMedio1,
                    opcionesPastillaPuente[index]))

    listaPuentes = []
    for index, item in enumerate(puentes):
        listaPuentes.append(
            myModal('modalPuente' + index.__str__(), 'Escoge Puente', opcionesPuente1,
                    opcionesPuente[index]))

    listaTonos1 = []
    for index, item in enumerate(tonos1):
        listaTonos1.append(
            myModal('modalTono1' + index.__str__(), 'Escoge Tono1', opcionesTono11,
                    opcionesTono1[index]))

    listaTonos2 = []
    for index, item in enumerate(tonos2):
        listaTonos2.append(
            myModal('modalTono2' + index.__str__(), 'Escoge Tono2', opcionesTono21,
                    opcionesTono2[index]))

    listaVolumenes = []
    for index, item in enumerate(volumenes):
        listaVolumenes.append(
            myModal('modalVolumen' + index.__str__(), 'Escoge Volumen', opcionesVolumen1,
                    opcionesVolumen[index]))

    listaTapas = []
    for index, item in enumerate(tapas):
        listaTapas.append(
            myModal('modalTapa' + index.__str__(), 'Escoge  Tapa', opcionesTapa1,
                    opcionesTapa[index]))

    listaChapas = []
    for index, item in enumerate(chapas):
        listaChapas.append(
            myModal('modalChapa' + index.__str__(), 'Escoge  Chapa', opcionesChapa1,
                    opcionesChapa[index]))

    listaJacks = []
    for index, item in enumerate(jacks):
        listaJacks.append(
            myModal('modalJack' + index.__str__(), 'Escoge  Jack', opcionesJack1,
                    opcionesJack1[index]))

    lista = [
        listaCuerpos,
        listaGolpeadores,
        listaMastiles,
        listaDiapasones,
        listaPastillasMastil,
        listaPastillasMedio,
        listaPastillasPuente,
        listaPuentes,
        listaTonos1,
        listaTonos2,
        listaVolumenes,
        listaTapas,
        listaChapas,
        listaJacks
    ]
    return render_template('loader.html', mytitle=title, lista=lista)
