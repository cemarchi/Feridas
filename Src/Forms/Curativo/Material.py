from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class Material(Form):
    nome = StringField('nome', validators=[DataRequired(message='Procedimento é requerido.')])
