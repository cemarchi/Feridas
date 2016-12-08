from flask_security import UserMixin
from flask.ext import bcrypt
from datetime import datetime

from Src import db


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False)
    autenticado = db.Column(db.Boolean, nullable=False)
    confirmado_em = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, email, senha, ativo=True, autenticado=True):
        self.nome = nome
        self.email = email
        self.senha = bcrypt.generate_password_hash(senha)
        self.ativo = ativo
        self.confirmado_em = datetime.utcnow()
        self.autenticado = autenticado

    def is_active(self):
        return self.ativo

    def senha_correta(self, senha_texto):
        return bcrypt.check_password_hash(self.senha, senha_texto)

    def to_json(self):
        return dict(nome=self.nome, email=self.email)