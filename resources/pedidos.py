from flask_restful import Resource
from models.pedidos import PedidosModel, PedidosParser

from flask_jwt import JWT, jwt_required

class Pedidos(Resource):
    @jwt_required()
    def get(self,num):
        pedido=PedidosModel.find_by_serial(num)
        if pedido:
            return pedido.json()
        return {'message':'Pedido not found'}, 404

    @jwt_required()
    def post(self,num):
        pedido = PedidosModel.find_by_serial(num)
        if pedido is None:
            parser = PedidosParser().put()
            data = parser.parse_args()
            mypedido = PedidosModel(data['pago_id'],data['factura'],num,data['modelo'],data['acabado']
                                    ,data['pastillas'],data['puente'],data['electronica'],data['clavijero']
                                    ,data['nombre'],data['direccion'],data['telefono'],
                                    data['email'],data['precio'],data['fecha'],data['observaciones'])
            mypedido.insert_to_db()
            return mypedido.json()
        return {'message:' 'Pedido con ese numero de serie ya exites'}, 400

    @jwt_required()
    def put(self,num):
        pedido = PedidosModel.find_by_serial(num)
        if pedido:
            parser = PedidosParser().put()
            data = parser.parse_args()
            if data['pago_id']:
                pedido.pago_id = data['pago_id']
            if data['factura']:
                pedido.factura = data['factura']
            if data['numero_serie']:
                pedido.numero_serie = data['numero_serie']
            if data['modelo']:
                pedido.modelo = data['modelo']
            if data['acabado']:
                pedido.acabado = data['acabado']
            if data['pastillas']:
                pedido.pastillas = data['pastillas']
            if data['puente']:
                pedido.puente = data['puente']
            if data['electronica']:
                pedido.electronica = data['electronica']
            if data['clavijero']:
                pedido.clavijero = data['clavijero']

            if data['nombre']:
                pedido.nombre = data['nombre']
            if data['direccion']:
                pedido.direccion = data['direccion']
            if data['telefono']:
                pedido.telefono = data['telefono']
            if data['email']:
                pedido.email = data['email']

            if data['precio']:
                pedido.precio = data['precio']
            if data['fecha']:
                pedido.fecha = data['fecha']
            if data['observaciones']:
                pedido.observaciones = data['observaciones']
            pedido.actualizar()
            return pedido.json(), 200
        return {'message':'Pedido not found'}, 404

    @jwt_required()
    def delete(self,num):
        pedido = PedidosModel.find_by_name(num)
        if pedido:
            pedido.delete_from_db()
            return pedido.json(), 204
        return {'message:' 'El pedido ya no existe'}, 404

class PedidosList(Resource):
    @jwt_required()
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