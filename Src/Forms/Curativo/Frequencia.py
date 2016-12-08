from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class Frequencia(Form):
    nome = StringField('nome', validators=[DataRequired(message='Frequência de curativo é requerido.')])
