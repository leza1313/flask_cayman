from flask_restful import Resource
from models.editor import Partes3DModel,Opciones3DModel,Precios3DModel

class Partes3D(Resource):

    def get(self):
        return [parte.json() for parte in Partes3DModel.query.all()]


class Opciones3D(Resource):

    def get(self,parte3D):
        return [opcion.json() for opcion in Opciones3DModel.find_by_parte(parte3D)]

class TodasOpciones3D(Resource):

    def get(self):
        return [opcion.json() for opcion in Opciones3DModel.query.all()]

class Precio3D(Resource):

    def get(self,parte3D,material):
        return [Precios3DModel.find_by_parte_material(parte3D,material).json()]

class TodosPrecio3D(Resource):

    def get(self, parte3D):
        return [opcion.json() for opcion in Precios3DModel.find_by_parte(parte3D)]