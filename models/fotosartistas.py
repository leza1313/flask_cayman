from connection import db

class FotosArtistasModel(db.Model):
    __tablename__ = 'fotosartistas'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    url = db.Column(db.String(150))
    artista = db.Column(db.Integer, db.ForeignKey('artistas.id'))


    def __init__(self,nombre,url,artista):
        self.nombre=nombre
        self.url=url
        self.artista=artista

    @classmethod
    def find_by_name(cls, url):
        return cls.query.filter_by(url=url).first()

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()