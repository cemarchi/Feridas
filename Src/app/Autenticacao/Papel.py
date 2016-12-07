from flask_security import RoleMixin, UserMixin

from Src.app import db


class Papel(db.Model, RoleMixin):
    __tablename__ = 'papel'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
