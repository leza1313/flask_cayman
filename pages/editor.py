import os
from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask import current_app as app
from flask_login import login_required
from werkzeug.utils import secure_filename

editor = Blueprint('editor', __name__)
from models.editor import Partes3DModel,Opciones3DModel,Precios3DModel, ModelosModel

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


@editor.route("/nuevo/modelo", methods=['GET','POST'])
@login_required
def nuevoModelo():
    if request.method == 'POST':

        modelo = request.form['modelo']
        static = os.path.join(app.config['UPLOAD_FOLDER'])
        print(static+'/modelos')

        myparte=ModelosModel(modelo)
        myparte.insert_to_db()
        flash('Exito: Se ha anadido correctamente el modelo')
        return render_template('nuevomodelo.html')

    modelos=ModelosModel.query.all()
    return render_template('nuevomodelo.html',mytitle='Nuevo Modelo',modelos=modelos)


@editor.route("/upload/json", methods=['GET','POST'])
@login_required
def nuevoJSON():
    if request.method == 'POST':
        print(request.form)
        print(request.files)
        modelo = request.form['modelo']


        f1 = request.files['file']
        static = os.path.join(app.config['UPLOAD_FOLDER'])
        rutaJSON = static + '/' + 'modelos/' + modelo

        if not (os.path.isdir(rutaJSON)):
            os.mkdir(rutaJSON)
        f1.save(os.path.join(rutaJSON, secure_filename(f1.filename)))

        f2 = request.files['file2']
        rutaFoto = static + '/' + 'img'
        f2.save(os.path.join(rutaFoto, secure_filename(f2.filename)))

        nombre = request.form['nombre']
        pieza = request.form['pieza']
        x = request.form['x']
        y = request.form['y']
        z = request.form['z']

        jsonPath = 'static/modelos/' + modelo + '/' + secure_filename(f1.filename)
        fotoPath = secure_filename(f2.filename)
        myparte=Partes3DModel(nombre,pieza,modelo,x,y,z,jsonPath,fotoPath)
        myparte.insert_to_db()
        flash('Exito: Se ha anadido correctamente el modelo')
        return render_template('uploadJSON.html')

    modelos=ModelosModel.query.all()
    return render_template('uploadJSON.html',mytitle='Nuevo JSON',modelos=modelos)


@editor.route("/upload/textura", methods=['GET','POST'])
@login_required
def nuevoTextura():
    if request.method == 'POST':

        print(request.form)
        f1 = request.files['file']
        static=os.path.join(app.config['UPLOAD_FOLDER'])
        rutaTextura=static+'/'+'modelos/'+request.form['modelo']+'/texturas'
        if not (os.path.isdir(rutaTextura)):
            os.mkdir(rutaTextura)
        f1.save(os.path.join(rutaTextura, secure_filename(f1.filename)))

        f2 = request.files['file2']
        rutaFoto = static + '/' + 'img'
        f2.save(os.path.join(rutaFoto, secure_filename(f2.filename)))

        nombre=request.form['nombre']
        parte3D=request.form['partes3Dlist']
        texturaPath='static/modelos/' + request.form['modelo'] + '/texturas/' +secure_filename(f1.filename)
        fotoPath=secure_filename(f2.filename)


        mytextura=Opciones3DModel(nombre,texturaPath,fotoPath,parte3D)
        mytextura.insert_to_db()
        flash('Exito: Se ha anadido correctamente la textura')
        return render_template('uploadTextura.html')

    partes=Partes3DModel.query.all()
    modelos=ModelosModel.query.all()
    return render_template('uploadTextura.html',mytitle='Nueva Textura',partes=partes, modelos=modelos)

@editor.route("/editor")
def html():
    title = 'Taller Custom'

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
    print(cuerpos)
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

    """opcionesModelo1=[]
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
        opcionesJack1.append(aux)"""

    ########################################
    ##LISTA DE LOS MODELOS CON SUS OPCIONES#
    ########################################

    #Ya actualizo los Body2 de los modal en JS mediante AJAX.
    #Quitar todas estas listas dentro de listas
    #Y dejar unicamente Lista->ListaCuerpos->

    """listaCuerpos=[]
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
                    opcionesJack1[index]))"""

    lista = [
        cuerpos,
        """listaGolpeadores,
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
        listaJacks"""
    ]
    #print(lista[0][0].opcionesModelo[1].modelo)
    return render_template('loader.html', mytitle=title, lista=lista)

