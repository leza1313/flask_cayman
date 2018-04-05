from connection import db
from flask_login import UserMixin


class UserModel(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24),unique=True)
    password = db.Column(db.String(80))

    def __init__(self, nombre, password):
        self.nombre=nombre
        self.password=password

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(nombre=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()