from connection import db

class Partes3DModel(db.Model):
    __tablename__ = 'partes3D'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80))
    pieza = db.Column(db.String(80))
    modelo = db.Column(db.String(80))
    x = db.Column(db.Float)
    y = db.Column(db.Float)
    z = db.Column(db.Float)
    rutaJSON = db.Column(db.String(200))
    foto = db.Column(db.String(200))
    opciones3D = db.relationship('Opciones3DModel')
    precio3D = db.relationship('Precios3DModel')


    def __init__(self,nombre,pieza,modelo,x,y,z,rutaJSON,foto):
        self.nombre = nombre
        self.pieza = pieza
        self.modelo = modelo
        self.x = x
        self.y = y
        self.z = z
        self.rutaJSON = rutaJSON
        self.foto = foto

    def json(self):
        return {'id':self.id,
                'nombre': self.nombre,
                'pieza': self.pieza,
                'modelo': self.modelo,
                'x': self.x,
                'y': self.y,
                'z': self.z,
                'rutaJSON': self.rutaJSON,
                'foto': self.foto
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_pieza(cls, pieza):
        return cls.query.filter_by(pieza=pieza).all()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class Opciones3DModel(db.Model):
    __tablename__ = 'opcionesPartes3D'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80))
    rutaTextura = db.Column(db.String(200))
    foto = db.Column(db.String(200))
    parte3D = db.Column(db.Integer, db.ForeignKey('partes3D.id'))


    def __init__(self,nombre,rutaTextura,foto,parte3D):
        self.nombre = nombre
        self.rutaTextura = rutaTextura
        self.foto = foto
        self.parte3D = parte3D

    def json(self):
        return {'nombre': self.nombre,
                'rutaTextura': self.rutaTextura,
                'foto': self.foto,
                'parte3D': self.parte3D
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_parte(cls, _id):
        return cls.query.filter_by(parte3D=_id).all()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

class Precios3DModel(db.Model):
    __tablename__ = 'precios3D'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parte3D = db.Column(db.Integer, db.ForeignKey('partes3D.id'))
    material = db.Column(db.String(80))
    precio = db.Column(db.Float)


    def __init__(self,parte3D,material,precio):
        self.parte3D = parte3D
        self.material = material
        self.precio = precio

    def json(self):
        return {'parte3D': self.parte3D,
                'material': self.material,
                'precio': self.precio
                }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

