from connection import db

class PedidosModel(db.Model):
    __tablename__ = 'pedidos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    numero_serie = db.Column(db.String(24))
    modelo = db.Column(db.String(24))
    acabado = db.Column(db.String(24))
    pastillas = db.Column(db.String(24))
    puente = db.Column(db.String(24))
    electronica = db.Column(db.String(24))
    clavijero = db.Column(db.String(24))

    nombre = db.Column(db.String(24))
    direccion = db.Column(db.String(500))
    telefono = db.Column(db.String(24))
    email = db.Column(db.String(24))

    precio = db.Column(db.String(24))
    fecha = db.Column(db.DateTime)
    observaciones = db.Column(db.Text)

    def __init__(self,numero_serie,modelo,acabado,pastillas,puente,electronica,clavijero
                 , nombre,direccion,telefono,email
                 , precio,fecha,observaciones):
        self.numero_serie=numero_serie
        self.modelo=modelo
        self.acabado=acabado
        self.pastillas=pastillas
        self.puente=puente
        self.electronica=electronica
        self.clavijero=clavijero

        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.email=email

        self.precio=precio
        self.fecha=fecha
        self.observaciones=observaciones

    def json(self):
        #TODO
        pass

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