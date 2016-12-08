from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired


class ProcedimentoMaterial(Form):
    procedimento_id = IntegerField('procedimento_id', validators=[DataRequired(message='Procedimento é requerido.')])
    material_id = IntegerField('material_id', validators=[DataRequired(message='Material é requerido.')])
