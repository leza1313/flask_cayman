from connection import db

class GaleriaModel(db.Model):
    __tablename__ = 'galeria'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(150))
    alt = db.Column(db.String(150))

    def __init__(self,url,alt):
        self.url = url
        self.alt =  alt

    @classmethod
    def find_by_name(cls, url):
        return cls.query.filter_by(url=url).first()

    def json(self):
        return {'id': self.id,
                'url': self.url,
                'alt': self.alt,}

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def actualizar(self):
        db.session.commit()