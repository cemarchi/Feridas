from flask_wtf import Form
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired


class UsuarioAutenticacao(Form):
    senha = PasswordField('senha', validators=[DataRequired(message='senha é requerida'),
                                               validators.length(min=4, max=10, message='senha deve possuir entre 4 a 10 caracteres')])
    usuario = StringField('email', validators=[DataRequired(message='e-mail é requerido'),
                                               validators.length(min=3, max=20, message='email deve possuir entre 3 a 20 caracteres'),
                                               validators.email(message='e-mail inválido')])
