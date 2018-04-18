from flask_restful import Resource
from models.pedidos import PedidosModel

from flask_jwt import JWT, jwt_required

class Pedidos(Resource):
    @jwt_required()
    def get(self,num):
        pedido=PedidosModel.find_by_serial(num)
        if pedido:
            return pedido.json()
        return {'message':'Pedido not found'}, 404
    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

class PedidosList(Resource):
    @jwt_required
    def get(self):
        return {'Pedidos': [pedido.json() for pedido in PedidosModel.query.all()]}

class TopModelo(Resource):
    def get(self):
        result = PedidosModel.countModelo()
        return {'Top Modelos':[{item[0]:item[1]} for item in result]}
class CountEsteMes(Resource):
    def get(self):
        result = PedidosModel.countEsteMes()
        return {'Ventas este mes': result[0][0]}