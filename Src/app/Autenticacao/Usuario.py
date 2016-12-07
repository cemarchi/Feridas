from flask_security import UserMixin
from flask.ext import bcrypt
import datetime

from Src.Main import db


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    senha = db.Column(db.String(255), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    confirmado_em = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, email, senha, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = bcrypt.generate_password_hash(senha)
        self.ativo = ativo
        self.confirmado_em = datetime.utcnow()

    def senha_correta(self, plaintext):
        return bcrypt.check_password_hash(self.__senha, plaintext)