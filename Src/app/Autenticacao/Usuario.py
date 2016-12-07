from flask_security import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from flask.ext import bcrypt

from Src.app import db

from Src.App.Autenticacao.PapeisUsuario import PapeisUsuario


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    __senha = db.Column(db.String(255), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    confirmado_em = db.Column(db.DateTime, nullable=False)
    papeis = db.relationship('Papel', secondary=PapeisUsuario,
                             backref=db.backref('usuarios', lazy='dynamic'))

    @hybrid_property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, plaintext):
        self.__senha = bcrypt.generate_password_hash(plaintext)

    def senha_correta(self, plaintext)
        return bcrypt.check_password_hash(self.__senha, plaintext)