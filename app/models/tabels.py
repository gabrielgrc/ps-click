from app import db

class Folder(db.Model):
    __tablename__ = "folders"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    #aqui pensar sobre usar ou não, pois na doc. não aparece mais
    #def __init__(self, name):
    #   self.name = name

    def __repr__(self):
        return "<Folder %r>" % self.name