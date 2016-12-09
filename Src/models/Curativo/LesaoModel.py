from Src import db


class LesaoModel(db.Model):
    __tablename__ = 'lesao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    def __init__(self, nome, ativo=True):
        self.nome = nome
        self.ativo = ativo

    def to_json(self):
        return dict(id=self.id, nome=self.nome)