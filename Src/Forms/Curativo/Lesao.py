from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class Lesao(Form):
    nome = StringField('nome', validators=[DataRequired(message='Lesão é requerida.')])
