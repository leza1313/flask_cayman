from connection import db

class GaleriaModel(db.Model):
    __tablename__ = 'galeria'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(150))
    alt = db.Column(db.String(150))

    def __init__(self,url,alt):
        self.url = url
        self.alt =  alt