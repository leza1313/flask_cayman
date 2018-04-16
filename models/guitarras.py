from connection import db

class GuitarrasModel(db.Model):
    __tablename__ = 'guitarras'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    descripcion = db.Column(db.Text)

    acabado = db.Column(db.String(24))
    pastillas = db.Column(db.String(24))
    puente = db.Column(db.String(24))
    electronica = db.Column(db.String(24))
    clavijero = db.Column(db.String(24))

    boton = db.Column(db.Text)
    precio = db.Column(db.Integer)

    fotopal = db.Column(db.String(150))
    fotopalalt = db.Column(db.String(150))
    fotos = db.relationship('FotosGuitarrasModel')

    def __init__(self,nombre,descripcion,acabado,pastillas,puente,electronica,clavijero, boton,precio,fotopal,fotopalalt):
        self.nombre=nombre
        self.descripcion=descripcion
        self.boton=boton
        self.precio=precio
        self.acabado=acabado
        self.pastillas=pastillas
        self.puente=puente
        self.electronica=electronica
        self.clavijero=clavijero
        self.fotopal=fotopal
        self.fotopalalt=fotopalalt

    def json(self):
        return {'id': self.id,
                'nombre': self.nombre,
                'descripcion': self.descripcion,
                'acabado': self.acabado,
                'pastillas': self.pastillas,
                'puente': self.puente,
                'electronica': self.electronica,
                'clavijero': self.clavijero,
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