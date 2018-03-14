from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class GuitarrasModel(db.Model):
    __tablename__ = 'guitarras'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    foto = db.Column(db.String(150))
    descripcion = db.Column(db.String(500))

    def __init__(self,id,nombre,foto,descripcion):
        self.id=id
        self.nombre=nombre
        self.foto=foto
        self.descripcion=descripcion

    def json(self):
        return {'id': self.id,
                'nombre': self.nombre,
                'foto': self.foto,
                'descripcion': self.descripcion}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(nombre=name).first()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()