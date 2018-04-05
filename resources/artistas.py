from flask_restful import Resource
from models.artistas import ArtistasModel

from flask_jwt import JWT, jwt_required


class Artistas(Resource):

    @jwt_required()
    def get(self,name):
        artista=ArtistasModel.find_by_name(name)
        if artista:
            return artista.json()
        return {'message': 'Artista not found'}, 404
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

class ArtistasList(Resource):

    def get(self):
        return {'Artistas': [artista.json() for artista in ArtistasModel.query.all()]}