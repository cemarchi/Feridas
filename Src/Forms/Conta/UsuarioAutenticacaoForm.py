from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UsuarioAutenticacaoForm(Form):
    senha = PasswordField('senha', validators=[DataRequired(message='Senha é requerida.'),
                                               Length(min=4, max=10, message='Senha deve possuir entre 4 a 10 caracteres.')])
    usuario = StringField('usuario', validators=[DataRequired(message='Usuário é requerido.'),
                                                 Length(min=3, max=20, message='Usuário deve possuir entre 3 a 20 caracteres.'),
                                                 Email(message='Usuário deve conter um e-mail inválido.')])
