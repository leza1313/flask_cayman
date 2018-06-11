from flask_restful import Resource
from models.editor import Partes3DModel,Opciones3DModel,Precios3DModel

class Partes3D(Resource):

    def get(self):
        return [parte.json() for parte in Partes3DModel.query.all()]

class Parte3D(Resource):

    def get(self,parte3D):
        parte = Partes3DModel.find_by_id(parte3D)
        if parte:
            return [parte.json()]
        return [{'message': 'Precio not found'}], 404


class Opciones3D(Resource):

    def get(self,parte3D):
        return [opcion.json() for opcion in Opciones3DModel.find_by_parte(parte3D)]

class TodasOpciones3D(Resource):

    def get(self):
        return [opcion.json() for opcion in Opciones3DModel.query.all()]

class Precio3D(Resource):

    def get(self,parte3D,material):
        precio = Precios3DModel.find_by_parte_material(parte3D,material)
        if precio:
            return [precio.json()]
        return [{'message': 'Precio not found'}], 404

class TodosPrecio3D(Resource):

    def get(self, parte3D):
        return [opcion.json() for opcion in Precios3DModel.find_by_parte(parte3D)]

class PastillasModelo(Resource):

    def get(self, modelo,past):

        pastillas=Partes3DModel.query.filter_by(pieza=past)
        pastMod=pastillas.filter(Partes3DModel.modelo==modelo).all()
        return [opcion.json() for opcion in pastMod]

class ModeloComponentes(Resource):

    def get(self, modelo):
        defecto=Partes3DModel.query.filter_by(modelo=modelo).all()
        aux=[]
        for opcion in defecto:
            if opcion.pieza!='Cuerpo' and opcion.pieza!='PastillaMastil' and opcion.pieza!='PastillaMedio' and opcion.pieza!='PastillaPuente':
                aux.append(opcion)
        return [opcion.json() for opcion in aux]

class ModeloDefecto(Resource):
    """0,'#modalCuerpo0'
    1,'#modalGolpeador0'
    2,'#modalMastil0'
    3,'#modalDiapason0'
    4,'#modalPastillaMastil0'
    5,'#modalPastillaMedio0'
    6,'#modalPastillaPuente0'
    7,'#modalPuente0'
    8,'#modalTono10'
    9,'#modalTono20'
    10,'#modalVolumen0'
    11,'#modalTapa0'
    12,'#modalChapa0'
    13,'#modalJack0'
    14,'#modalClavijero0'
    15,'#modalCejuela0'
    16,'#modalSwitch0'"""
    def get(self, modelo):
        result=[]
        defecto=Partes3DModel.query.filter_by(modelo=modelo)

        cuerpo=defecto.filter(Partes3DModel.pieza=='Cuerpo').first()
        if not cuerpo:
            cuerpo=Partes3DModel('','','','','','','','')
        result.append(cuerpo.json())

        golpeador=defecto.filter(Partes3DModel.pieza=='Golpeador').first()
        if not golpeador:
            golpeador = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(golpeador.json())

        mastil=defecto.filter(Partes3DModel.pieza=='Mastil').first()
        if not mastil:
            mastil = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(mastil.json())

        diapason = defecto.filter(Partes3DModel.pieza == 'Diapason').first()
        if not diapason:
            diapason = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(diapason.json())

        PastillaMastil = defecto.filter(Partes3DModel.pieza == 'PastillaMastil').first()
        if not PastillaMastil:
            PastillaMastil = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(PastillaMastil.json())

        PastillaMedio = defecto.filter(Partes3DModel.pieza == 'PastillaMedio').first()
        if not PastillaMedio:
            PastillaMedio = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(PastillaMedio.json())

        PastillaPuente = defecto.filter(Partes3DModel.pieza == 'PastillaPuente').first()
        if not PastillaPuente:
            PastillaPuente = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(PastillaPuente.json())

        Puente = defecto.filter(Partes3DModel.pieza == 'Puente').first()
        if not Puente:
            Puente = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Puente.json())

        Tono1 = defecto.filter(Partes3DModel.pieza == 'Tono1').first()
        if not Tono1:
            Tono1 = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Tono1.json())

        Tono2 = defecto.filter(Partes3DModel.pieza == 'Tono2').first()
        if not Tono2:
            Tono2 = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Tono2.json())

        Volumen = defecto.filter(Partes3DModel.pieza == 'Volumen').first()
        if not Volumen:
            Volumen = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Volumen.json())

        Tapa = defecto.filter(Partes3DModel.pieza == 'Tapa').first()
        if not Tapa:
            Tapa = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Tapa.json())

        Chapa = defecto.filter(Partes3DModel.pieza == 'Chapa').first()
        if not Chapa:
            Chapa = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Chapa.json())

        Jack = defecto.filter(Partes3DModel.pieza == 'Jack').first()
        if not Jack:
            Jack = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Jack.json())

        Clavijero = defecto.filter(Partes3DModel.pieza == 'Clavijero').first()
        if not Clavijero:
            Clavijero = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Clavijero.json())

        Cejuela = defecto.filter(Partes3DModel.pieza == 'Cejuela').first()
        if not Cejuela:
            Cejuela = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Cejuela.json())

        Switch = defecto.filter(Partes3DModel.pieza == 'Switch').first()
        if not Switch:
            Switch = Partes3DModel('', '', '', '', '', '', '', '')
        result.append(Switch.json())

        return result
