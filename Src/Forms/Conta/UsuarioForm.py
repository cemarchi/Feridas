from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UsuarioForm(Form):
    senha = PasswordField('senha', validators=[DataRequired(message='Senha é requerida.'),
                                               Length(min=4, max=10, message='Senha deve possuir entre 4 a 10 caracteres.')])
    email = StringField('email', validators=[DataRequired(message='E-mail é requerido.'),
                                             Length(min=3, max=20, message='E-mail deve possuir entre 3 a 20 caracteres.'),
                                             Email(message='E-mail inválido.')])
    nome = StringField('nome', validators=[DataRequired(message='Nome é requerido.'),
                                           Length(min=3, max=50, message='Nome deve possuir entre 3 a 50 caracteres.')])

