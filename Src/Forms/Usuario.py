from flask_wtf import Form
from wtforms import StringField, PasswordField, validators


class Usuario(Form):
    senha = PasswordField('senha', validators=[validators.required(message='senha é requerida'),
                                               validators.length(min=4, max=10, message='senha deve possuir entre 4 a 10 caracteres')])
    email = StringField('email', validators=[validators.required(message='e-mail é requerido'),
                                             validators.length(min=3, max=20, message='email deve possuir entre 3 a 20 caracteres'),
                                             validators.email(message='e-mail inválido')])
    nome = StringField('nome', validators=[validators.required(message='nome é requerido'),
                                           validators.length(min=3, max=50, message='nome deve possuir entre 3 a 50 caracteres')])

