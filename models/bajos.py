from connection import db

class BajosModel(db.Model):
    __tablename__ = 'bajos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    descripcion = db.Column(db.Text)
    fotopal = db.Column(db.String(500))
    fotos=db.relationship("FotosBajosModel")

    def __init__(self,nombre,descripcion,fotopal):
        self.nombre=nombre
        self.descripcion=descripcion
        self.fotopal=fotopal

    def json(self):
        return {'id': self.id,
                'nombre': self.nombre,
                'descripcion': self.descripcion,
                'fotopal': self.fotopal}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(nombre=name).first()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        [item.delete_from_db() for item in self.fotos]
        db.session.delete(self)
        db.session.commit()

    def actualizar(self):
        db.session.commit()