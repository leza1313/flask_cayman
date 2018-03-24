from connection import db

class GuitarrasModel(db.Model):
    __tablename__ = 'guitarras'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    foto1 = db.Column(db.String(150))
    foto2 = db.Column(db.String(150))
    foto3 = db.Column(db.String(150))
    foto4 = db.Column(db.String(150))
    descripcion = db.Column(db.String(500))

    def __init__(self,nombre,foto1,foto2,foto3,foto4,descripcion):
        self.nombre=nombre
        self.foto1=foto1
        self.foto2=foto2
        self.foto3=foto3
        self.foto4=foto4
        self.descripcion=descripcion

    def json(self):
        return {'id': self.id,
                'nombre': self.nombre,
                'foto1': self.foto1,
                'foto2': self.foto2,
                'foto3': self.foto3,
                'foto4': self.foto4,
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

    def actualizar(self):
        db.session.commit()