from flask_restful import reqparse
from sqlalchemy import func, extract
import datetime

from connection import db

class PresupuestosModel(db.Model):
    __tablename__ = 'presupuestos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80))
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(128))

    fecha = db.Column(db.DateTime)

    modelo = db.Column(db.String(80))
    maderaCuerpo = db.Column(db.String(80))
    maderaDiapason = db.Column(db.String(80))
    maderaMastil = db.Column(db.String(80))
    mastil = db.Column(db.String(80))
    pastillaMastil = db.Column(db.String(80))
    pastillaMedio = db.Column(db.String(80))
    pastillaPuente = db.Column(db.String(80))
    puente = db.Column(db.String(80))
    tono1 = db.Column(db.String(80))
    tono2 = db.Column(db.String(80))
    volumen = db.Column(db.String(80))
    tapa = db.Column(db.String(80))
    chapa = db.Column(db.String(80))
    jack = db.Column(db.String(80))
    #clavijero = db.Column(db.String(80))

    acabado = db.Column(db.String(80))
    colorCuerpo = db.Column(db.String(80))
    colorGolpeador = db.Column(db.String(80))
    colorPastillaMastil = db.Column(db.String(80))
    colorPastillaMedio = db.Column(db.String(80))
    colorPastillaPuente = db.Column(db.String(80))
    colorPuente = db.Column(db.String(80))
    #colorClavijero = db.Column(db.String(80))
    colorTono1 = db.Column(db.String(80))
    colorTono2 = db.Column(db.String(80))
    colorVolumen = db.Column(db.String(80))
    colorTapa = db.Column(db.String(80))
    colorChapa = db.Column(db.String(80))
    colorJack = db.Column(db.String(80))

    comentarios = db.Column(db.Text)

    def __init__(self,nombre,telefono,email,fecha,modelo,maderaCuerpo,maderaDiapason,maderaMastil,mastil,
                 pastillaMastil,pastillaMedio,pastillaPuente,puente,tono1,tono2,volumen,tapa,chapa,jack,
                 acabado,
                 colorCuerpo,colorGolpeador,colorPastillaMastil,colorPastillaMedio,colorPastillaPuente,
                 colorPuente,colorTono1,colorTono2,colorVolumen,colorTapa,colorChapa,colorJack,comentarios):

        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.fecha = fecha
        self.modelo = modelo
        self.maderaCuerpo = maderaCuerpo
        self.maderaDiapason = maderaDiapason
        self.maderaMastil =maderaMastil
        self.mastil = mastil
        self.pastillaMastil = pastillaMastil
        self.pastillaMedio = pastillaMedio
        self.pastillaPuente = pastillaPuente
        self.puente = puente
        self.tono1 = tono1
        self.tono2 = tono2
        self.volumen = volumen
        self.tapa = tapa
        self.chapa = chapa
        self.jack = jack
        self.acabado = acabado
        self.colorCuerpo = colorCuerpo
        self.colorGolpeador = colorGolpeador
        self.colorPastillaMastil = colorPastillaMastil
        self.colorPastillaMedio = colorPastillaMedio
        self.colorPastillaPuente = colorPastillaPuente
        self.colorPuente = colorPuente
        self.colorTono1 = colorTono1
        self.colorTono2 = colorTono2
        self.colorVolumen = colorVolumen
        self.colorTapa = colorTapa
        self.colorChapa = colorChapa
        self.colorJack = colorJack
        self.comentarios = comentarios

    def json(self):
        return {'id':self.id,
                'nombre': self.nombre,
                'telefono': self.telefono,
                'email ': self.email,
                'fecha': self.fecha,
                'modelo': self.modelo,
                'maderaCuerpo': self.maderaCuerpo,
                'maderaDiapason': self.maderaDiapason,
                'maderaMastil': self.maderaMastil,
                'pastillaMastil': self.pastillaMastil,
                'pastillaMedio': self.pastillaMedio,
                'pastillaPuente': self.pastillaPuente,
                'puente': self.puente,
                'tono1': self.tono1,
                'tono2': self.tono2,
                'volumen': self.volumen,
                'tapa': self.tapa,
                'chapa': self.chapa,
                'jack': self.jack,
                'acabado': self.acabado,
                'colorCuerpo': self.colorCuerpo,
                'colorGolpeador': self.colorGolpeador,
                'colorPastillaMastil': self.colorPastillaMastil,
                'colorPastillaMedio': self.colorPastillaMedio,
                'colorPastillaPuente': self.colorPastillaPuente,
                'colorPuente': self.colorPuente,
                'colorTono1': self.colorTono1,
                'colorTono2': self.colorTono2,
                'colorVolumen': self.colorVolumen,
                'colorTapa': self.colorTapa,
                'colorChapa': self.colorChapa,
                'colorJack': self.colorJack,
                'comentarios': self.comentarios
        }

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


"""class PedidosParser():
    parser = reqparse.RequestParser()

    def post(self):
        PedidosParser.parser.add_argument('pago_id')
        return PedidosParser.parser

    def put(self):
        PedidosParser.parser.add_argument('pago_id')
        return PedidosParser.parser"""
