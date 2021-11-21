from .db import db


class Words(db.Model):
    __tabelname__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    words = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f"Words(id={self.id})"