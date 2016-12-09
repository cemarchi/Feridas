from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired


class CurativoForm(Form):
    material_limpeza_id = IntegerField('material_limpeza_id',
                                       validators=[DataRequired(message='Material de limpeza é requerido.')])
    material_oclusao_id = IntegerField('material_oclusao_id',
                                       validators=[DataRequired(message='Material de oclusão é requerido.')])
    material_fixacao_id = IntegerField('material_fixacao_id',
                                       validators=[DataRequired(message='Material de fixação é requerido.')])
    material_aplicacao_id = IntegerField('material_aplicacao_id',
                                         validators=[DataRequired(message='Material de aplicação é requerido.')])
    frequencia_id = IntegerField('frequencia_id',
                                 validators=[DataRequired(message='Frequência é requerido.')])
