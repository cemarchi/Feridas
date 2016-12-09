from Src.Models import db


class ProcedimentoMaterialModel(db.Model):
    __tablename__ = 'procedimento_material'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_material = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)
    id_procedimento = db.Column(db.Integer, db.ForeignKey('procedimento.id'), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    procedimento = db.relationship("ProcedimentoModel")
    material = db.relationship("MaterialModel")

    def __init__(self, id_procedimento, id_material, ativo=True):
        self.id_procedimento = id_procedimento
        self.id_material = id_material
        self.ativo = ativo

    def to_json(self):
        return dict(id=self.id,
                    id_procedimento=self.id_procedimento,
                    nome_procedimento=self.procedimento.nome,
                    id_material=self.id_material,
                    nome_material=self.material.nome)
