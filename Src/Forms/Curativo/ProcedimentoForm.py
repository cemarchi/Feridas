from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class ProcedimentoForm(Form):
    nome = StringField('nome', validators=[DataRequired(message='Procedimento é requerido.')])
