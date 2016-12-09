from sqlalchemy.orm import relationship

from Src import db


class CurativoModel(db.Model):
    __tablename__ = 'curativo'

    id_material_limpeza = db.Column(db.Integer, db.ForeignKey('procedimento_material.id'),
                                    autoincrement=False, primary_key=True)
    id_material_oclusao = db.Column(db.Integer, db.ForeignKey('procedimento_material.id'),
                                    autoincrement=False, primary_key=True)
    id_material_fixacao = db.Column(db.Integer, db.ForeignKey('procedimento_material.id'),
                                    autoincrement=False, primary_key=True, )
    id_material_aplicacao = db.Column(db.Integer, db.ForeignKey('procedimento_material.id'),
                                      autoincrement=False, primary_key=True, )
    id_frequencia = db.Column(db.Integer, db.ForeignKey('frequencia.id'), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    material_limpeza = db.relationship("ProcedimentoMaterialModel",
                                       uselist=False,
                                       foreign_keys=[id_material_limpeza])

    material_oclusao = db.relationship("ProcedimentoMaterialModel",
                                       uselist=False,
                                       foreign_keys=[id_material_oclusao])

    material_fixacao = db.relationship("ProcedimentoMaterialModel",
                                       uselist=False,
                                       foreign_keys=[id_material_fixacao])

    material_aplicacao = relationship("ProcedimentoMaterialModel",
                                      uselist=False,
                                      foreign_keys=[id_material_aplicacao])

    frequencia = relationship("FrequenciaModel",
                              uselist=False)

    def __init__(self, id_material_limpeza, id_material_oclusao,
                 id_material_fixacao, id_material_aplicacao, id_frequencia,
                 ativo=True):
        self.id_material_limpeza = id_material_limpeza
        self.id_material_oclusao = id_material_oclusao
        self.id_material_fixacao = id_material_fixacao
        self.id_material_aplicacao = id_material_aplicacao
        self.id_frequencia = id_frequencia
        self.ativo = ativo

    def to_json(self):
        return dict(id_material_limpeza=self.material_limpeza.material.id,
                    nome_material_limpeza=self.material_limpeza.material.nome)