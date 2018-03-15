from flask_restful import Resource
from models.bajos import BajosModel

class Bajos(Resource):

    def get(self,name):
        bajo=BajosModel.find_by_name(name)
        if bajo:
            return bajo.json()
        return {'message': 'Bajo not found'}, 404
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

class BajosList(Resource):

    def get(self):
        return {'Bajos': [bajo.json() for bajo in BajosModel.query.all()]}