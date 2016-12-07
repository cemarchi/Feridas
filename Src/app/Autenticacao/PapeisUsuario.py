from Src.app import db


class PapeisUsuario(db.Model):
    __tablename__ = 'papeis_usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE', nullable=False))
    papel_id = db.Column(db.Integer, db.ForeignKey('papel.id', ondelete='CASCADE', nullable=False))