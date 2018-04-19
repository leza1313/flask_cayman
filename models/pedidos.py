from flask_restful import reqparse
from sqlalchemy import func, extract
import datetime

from connection import db

class PedidosModel(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pago_id = db.Column(db.String(50), unique=True)
    factura = db.Column(db.String(50))

    numero_serie = db.Column(db.String(24), unique=True)
    modelo = db.Column(db.String(24))
    acabado = db.Column(db.String(24))
    pastillas = db.Column(db.String(24))
    puente = db.Column(db.String(24))
    electronica = db.Column(db.String(24))
    clavijero = db.Column(db.String(24))

    nombre = db.Column(db.String(128))
    direccion = db.Column(db.String(370))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(128))

    precio = db.Column(db.String(24))
    fecha = db.Column(db.DateTime)
    fecha_salida = db.Column(db.DateTime)
    observaciones = db.Column(db.Text)

    def __init__(self,pago_id,factura,numero_serie,modelo,acabado,pastillas,puente,electronica,clavijero
                 , nombre,direccion,telefono,email
                 , precio,fecha,observaciones):
        self.pago_id=pago_id
        self.factura=factura
        self.numero_serie=numero_serie
        self.modelo=modelo
        self.acabado=acabado
        self.pastillas=pastillas
        self.puente=puente
        self.electronica=electronica
        self.clavijero=clavijero

        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.email=email

        self.precio=precio
        self.fecha=fecha
        self.observaciones=observaciones

    def json(self):
        return {'id':self.id,
                'pago_id':self.pago_id,
                'factura':self.factura,
                'numero_serie':self.numero_serie,
                'modelo':self.modelo,
                'acabado':self.acabado,
                'pastillas':self.pastillas,
                'puente':self.puente,
                'electronica':self.electronica,
                'clavijero':self.clavijero,
                'nombre':self.nombre,
                'direccion':self.direccion,
                'telefono':self.telefono,
                'email':self.email,
                'precio':self.precio,
                'fecha':self.fecha.__str__(),
                'observaciones':self.observaciones}

    @classmethod
    def find_by_serial(cls,serial):
        return cls.query.filter_by(numero_serie=serial).first()

    @classmethod
    def find_last(cls):
        return cls.query.order_by(cls.id.desc()).first()

    @classmethod
    def countModelo(cls):
        return db.session.query(PedidosModel.modelo,func.count(PedidosModel.modelo)).group_by(PedidosModel.modelo).order_by(func.count(PedidosModel.modelo).desc()).all()

    @classmethod
    def countEsteMes(cls):
        today = datetime.datetime.today()
        month = today.month
        year = today.year
        result=db.session.execute('SELECT count(*) FROM pedidos WHERE extract(MONTH FROM fecha)= :val and EXTRACT(YEAR FROM fecha)= :val2',{'val':month,'val2':year}).fetchall()
        return result

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def actualizar(self):
        db.session.commit()


class PedidosParser():
    parser = reqparse.RequestParser()

    def post(self):
        PedidosParser.parser.add_argument('pago_id')
        PedidosParser.parser.add_argument('factura')
        PedidosParser.parser.add_argument('numero_serie', required=True)
        PedidosParser.parser.add_argument('modelo', required=True)
        PedidosParser.parser.add_argument('acabado')
        PedidosParser.parser.add_argument('pastillas')
        PedidosParser.parser.add_argument('puente')
        PedidosParser.parser.add_argument('electronica')
        PedidosParser.parser.add_argument('clavijero')

        PedidosParser.parser.add_argument('nombre', required=True)
        PedidosParser.parser.add_argument('direccion', required=True)
        PedidosParser.parser.add_argument('telefono', required=True)
        PedidosParser.parser.add_argument('email', required=True)

        PedidosParser.parser.add_argument('precio', required=True)
        PedidosParser.parser.add_argument('fecha', required=True)
        PedidosParser.parser.add_argument('observaciones')
        return PedidosParser.parser

    def put(self):
        PedidosParser.parser.add_argument('pago_id')
        PedidosParser.parser.add_argument('factura')
        PedidosParser.parser.add_argument('numero_serie')
        PedidosParser.parser.add_argument('modelo')
        PedidosParser.parser.add_argument('acabado')
        PedidosParser.parser.add_argument('pastillas')
        PedidosParser.parser.add_argument('puente')
        PedidosParser.parser.add_argument('electronica')
        PedidosParser.parser.add_argument('clavijero')

        PedidosParser.parser.add_argument('nombre')
        PedidosParser.parser.add_argument('direccion')
        PedidosParser.parser.add_argument('telefono')
        PedidosParser.parser.add_argument('email')

        PedidosParser.parser.add_argument('precio')
        PedidosParser.parser.add_argument('fecha')
        PedidosParser.parser.add_argument('observaciones')
        PedidosParser.parser.add_argument('fecha_salida')
        return PedidosParser.parser
