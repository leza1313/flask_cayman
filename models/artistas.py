from connection import db

class ArtistasModel(db.Model):
    __tablename__ = 'artistas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    descripcion = db.Column(db.Text)
    fotopal = db.Column(db.String(150))
    fotopalalt = db.Column(db.String(150))
    fotos = db.relationship('FotosArtistasModel')

    def __init__(self,nombre,descripcion,fotopal,fotopalalt):
        self.nombre=nombre
        self.descripcion=descripcion
        self.fotopal=fotopal
        self.fotopalalt=fotopalalt

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
        db.session.delete(self)
        db.session.commit()

    def actualizar(self):
        db.session.commit()