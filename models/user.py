from connection import db
from flask_login import UserMixin


class UserModel(UserMixin,db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24),unique=True)
    password = db.Column(db.String(80))

    def __init__(self,id,nombre,password):
        self.id=id
        self.nombre=nombre
        self.password=password