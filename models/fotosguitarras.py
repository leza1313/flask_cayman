from connection import db

class FotosGuitarrasModel(db.Model):
    __tablename__ = 'fotosguitarras'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    url = db.Column(db.String(150))
    guitarra = db.Column(db.Integer, db.ForeignKey('guitarras.id'))


    def __init__(self,nombre,url,guitarra):
        self.nombre=nombre
        self.url=url
        self.guitarra=guitarra

    @classmethod
    def find_by_name(cls, url):
        return cls.query.filter_by(url=url).first()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()