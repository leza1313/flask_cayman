from connection import db

class ArtistasModel(db.Model):
    __tablename__ = 'artistas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    foto1 = db.Column(db.String(150))
    foto2 = db.Column(db.String(150))
    foto3 = db.Column(db.String(150))
    foto4 = db.Column(db.String(150))
    descripcion = db.Column(db.String(500))

    def __init__(self,id,nombre,foto1,foto2,foto3,foto4,descripcion):
        self.id=id
        self.nombre=nombre
        self.foto1=foto1
        self.foto2=foto2
        self.foto3=foto3
        self.foto4=foto4
        self.descripcion=descripcion