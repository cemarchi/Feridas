from Src.Models import db


class FrequenciaModel(db.Model):
    __tablename__ = 'frequencia'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(20), unique=True, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    def __init__(self, nome, ativo=True):
        self.nome = nome
        self.ativo = ativo

    def to_json(self):
        return dict(id=self.id, nome=self.nome)
