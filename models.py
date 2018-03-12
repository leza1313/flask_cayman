from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class guitarras(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(24))
    foto = db.Column(db.String(150))
    descripcion = db.Column(db.String(500))


    def __repr__(self):
        return '<Guitarra %r>' % self.id

