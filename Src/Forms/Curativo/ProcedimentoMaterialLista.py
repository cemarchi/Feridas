from flask_wtf import Form
from wtforms import FieldList, FormField

from Src.Forms.Curativo.ProcedimentoMaterial import ProcedimentoMaterial


class ProcedimentoMaterialLista(Form):
    procedimento_materiais = FieldList(FormField(ProcedimentoMaterial))
