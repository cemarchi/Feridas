from sqlalchemy.orm import relationship

from Src import db


class ProcedimentoMaterial(db.Model):
    __tablename__ = 'procedimento_material'

    id_material = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_procedimento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ativo = db.Column(db.Boolean, nullable=False)

    def __init__(self, id_procedimento, id_material, ativo=True):
        self.id_procedimento = id_procedimento
        self.id_material = id_material
        self.ativo = ativo

    def to_json(self):
        return dict(id_procedimento=self.id_procedimento,
                    id_material=self.id_material,
                    nome=self.nome)
