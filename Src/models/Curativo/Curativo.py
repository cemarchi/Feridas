from sqlalchemy.orm import relationship

from Src import db


class Material(db.Model):
    __tablename__ = 'curativo'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_material_id = db.Column(db.Integer, db.ForeignKey('tipo_material.id'))
    nome = db.Column(db.String(100), unique=True, nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)

    tipo_material = relationship('TipoMaterial',
                                 uselist=False,
                                 backref='material', lazy='dynamic',
                                 foreign_keys = 'TipoMaterial.id')

    def __init__(self, nome, ativo=True):
        self.nome = nome
        self.ativo = ativo

    def to_json(self):
        return dict(id=self.id, nome=self.nome)