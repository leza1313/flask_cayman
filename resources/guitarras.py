from flask_restful import Resource
from models.guitarras import GuitarrasModel

class Guitarras(Resource):

    def get(self,name):
        guitarra=GuitarrasModel.find_by_name(name)
        if guitarra:
            return guitarra.json()
        return {'message':'Guitarra not found'}, 404
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

class GuitarrasList(Resource):

    def get(self):
        return {'Guitarras': [guitarra.json() for guitarra in GuitarrasModel.query.all()]}