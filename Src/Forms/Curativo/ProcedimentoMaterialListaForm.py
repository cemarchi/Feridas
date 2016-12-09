from flask_wtf import Form
from wtforms import FieldList, FormField

from Src.Forms.Curativo.ProcedimentoMaterialForm import ProcedimentoMaterialForm


class ProcedimentoMaterialListaForm(Form):
    procedimentos_materiais = FieldList(FormField(ProcedimentoMaterialForm))
