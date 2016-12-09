from flask import Blueprint, request
from flask.ext.api import status
from flask.ext.login import login_required
from flask_json import as_json

from Src import db
from Src .Cache import cache
from Src.Forms.Curativo.LesaoForm import LesaoForm
from Src.Models.Curativo.LesaoModel import LesaoModel
from Src.Forms.Curativo.ProcedimentoForm import ProcedimentoForm
from Src.Models.Curativo.ProcedimentoModel import ProcedimentoModel
from Src.Forms.Curativo.MaterialForm import MaterialForm
from Src.Models.Curativo.MaterialModel import MaterialModel
from Src.Forms.Curativo.FrequenciaForm import FrequenciaForm
from Src.Models.Curativo.FrequenciaModel import FrequenciaModel
from Src.Forms.Curativo.ProcedimentoMaterialListaForm import ProcedimentoMaterialListaForm
from Src.Models.Curativo.ProcedimentoMaterialModel import ProcedimentoMaterialModel
from Src.Forms.Curativo.CurativoForm import CurativoForm
from Src.Models.Curativo.CurativoModel import CurativoModel

curativo = Blueprint('curativo', __name__)


@curativo.route("/lesoes", methods=["POST"])
@login_required
@as_json
def adicionar_lesao():
    form = LesaoForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Lesão inválida. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return {'descricao': mensagem_erro.strip()}, status.HTTP_400_BAD_REQUEST

    if not LesaoModel.query.filter_by(nome=form.nome.data).first():
        db.session.add(LesaoModel(form.nome.data))
        db.session.commit()

        return {'descricao': 'Lesão cadastrada com sucesso.'}, status.HTTP_201_CREATED

    return {'descricao': 'Impossível cadastrar a lesão.'}, status.HTTP_409_CONFLICT


@curativo.route("/lesoes", methods=["GET"])
@login_required
@cache.cached(300)
@as_json
def listar_lesoes():
    lesoes = LesaoModel.query.all()

    if any(lesoes):
        return {'descricao': [l.to_json() for l in lesoes]}, status.HTTP_200_OK

    return {'descricao': 'Nenhuma lesão encontrada.'}, status.HTTP_204_NO_CONTENT


@curativo.route("/materiais", methods=["POST"])
@login_required
@as_json
def adicionar_material():
    form = MaterialForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Material inválido. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return {'descricao': mensagem_erro.strip()}, status.HTTP_400_BAD_REQUEST

    if not MaterialModel.query.filter_by(nome=form.nome.data).first():
        db.session.add(MaterialModel(form.nome.data))
        db.session.commit()

        return {'descricao': 'Material cadastrado com sucesso.'}, status.HTTP_201_CREATED

    return {'descricao': 'Impossível cadastrar o material.'}, status.HTTP_409_CONFLICT


@curativo.route("/materiais", methods=["GET"])
@login_required
@cache.cached(300)
@as_json
def listar_materiais():
    materiais = MaterialModel.query.all()

    if any(materiais):
        return {'descricao': [m.to_json() for m in materiais]}, status.HTTP_200_OK

    return {'descricao': 'Nenhum material encontrado.'}, status.HTTP_204_NO_CONTENT


@curativo.route("/procedimentos", methods=["POST"])
@login_required
@as_json
def adicionar_procedimento():
    form = ProcedimentoForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Procedimento inválido. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return {'descricao': mensagem_erro.strip()}, status.HTTP_400_BAD_REQUEST

    if not ProcedimentoModel.query.filter_by(nome=form.nome.data).first():
        db.session.add(ProcedimentoModel(form.nome.data))
        db.session.commit()

        return {'descricao': 'Procedimento cadastrado com sucesso.'}, status.HTTP_201_CREATED

    return {'descricao': 'Impossível cadastrar o procedimento.'}, status.HTTP_409_CONFLICT


@curativo.route("/procedimentos", methods=["GET"])
@login_required
@cache.cached(300)
@as_json
def listar_procedimentos():
    procedimentos = ProcedimentoModel.query.all()

    if any(procedimentos):
        return {'detalhe': [p.to_json() for p in procedimentos]}, status.HTTP_200_OK

    return {'descricao': 'Nenhum procedimento encontrado.'}, status.HTTP_204_NO_CONTENT


@curativo.route("/freq_curativos", methods=["POST"])
@login_required
@as_json
def adicionar_frequencia():
    form = FrequenciaForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Frequência de curativo inválida. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return {'descricao': mensagem_erro.strip()}, status.HTTP_400_BAD_REQUEST

    if not FrequenciaModel.query.filter_by(nome=form.nome.data).first():
        db.session.add(FrequenciaModel(form.nome.data))
        db.session.commit()

        return {'descricao': 'Frequência de curativo cadastrado com sucesso.'}, status.HTTP_201_CREATED

    return {'descricao': 'Impossível cadastrar a frequência de curativo.'}, status.HTTP_409_CONFLICT


@curativo.route("/freq_curativos", methods=["GET"])
@login_required
@cache.cached(300)
@as_json
def listar_frequencia():
    frequencias = FrequenciaModel.query.all()

    if any(frequencias):
        return {'descricao': [f.to_json() for f in frequencias]}, status.HTTP_200_OK

    return {'descricao': 'Nenhuma frequência de curativo encontrada.'}, status.HTTP_204_NO_CONTENT


@curativo.route("/procedimentos/materiais", methods=["POST"])
@login_required
@as_json
def adicionar_procedimento_material():
    erro_mensagem = 'Impossível cadastrar os procedimento e materiais.'

    form = ProcedimentoMaterialListaForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.procedimentos_materiais.errors):
        return {'descricao': 'Materiais ou Procedimentos inválidos.'}, status.HTTP_400_BAD_REQUEST

    procedimentos_materiais = form.procedimentos_materiais.entries

    # sql lite não acheita clausula in com mais de duas colunas: workound
    procedimento_materiais_model = ProcedimentoMaterialModel.query \
        .with_entities(ProcedimentoMaterialModel.id_procedimento, ProcedimentoMaterialModel.id_material) \
        .all()

    if any([pm for pm in procedimentos_materiais if (pm.procedimento_id.data,
                                                     pm.material_id.data) in procedimento_materiais_model]):
        return {'descricao': erro_mensagem}, status.HTTP_409_CONFLICT

    try:
        db.session.bulk_save_objects([ProcedimentoMaterialModel(pm.procedimento_id.data,
                                                                pm.material_id.data)
                                      for pm in procedimentos_materiais])

        db.session.commit()

        message = 'Procedimentos e materiais cadastrados com sucesso.'
        status_http = status.HTTP_201_CREATED
    except Exception as ex:
        message = erro_mensagem
        status_http = status.HTTP_409_CONFLICT

    return {'descricao': message}, status_http


@curativo.route("/procedimentos/materiais", methods=["GET"])
@login_required
@cache.cached(300)
@as_json
def listar_procedimento_materiais():
    procedimentos_materiais = ProcedimentoMaterialModel.query.all()

    if any(procedimentos_materiais):
        return {'descricao': [pm.to_json() for pm in procedimentos_materiais]}, status.HTTP_200_OK

    return {'descricao': 'Nenhum procedimento com material encontrado.'}, status.HTTP_204_NO_CONTENT


@curativo.route("/curativos", methods=["POST"])
@login_required
@as_json
def adicionar_curativo():
    form = CurativoForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.material_limpeza_id.errors) or \
            any(form.material_oclusao_id.errors) or \
            any(form.material_fixacao_id.errors) or \
            any(form.material_aplicacao_id.errors) or \
            any(form.frequencia_id.errors):
        mensagem_erro = 'Curativo inválido. {0} {1} {2} {3} {4}'.format(
            ' '.join(form.material_limpeza_id.errors if form.material_limpeza_id.errors else ''),
            ' '.join(form.material_oclusao_id.errors if form.material_oclusao_id.errors else ''),
            ' '.join(form.material_fixacao_id.errors if form.material_fixacao_id.errors else ''),
            ' '.join(form.material_aplicacao_id.errors if form.material_aplicacao_id.errors else ''),
            ' '.join(form.frequencia_id.errors if form.frequencia_id.errors else ''))

        return {'descricao': mensagem_erro.strip()}, status.HTTP_400_BAD_REQUEST

    if CurativoModel.query.filter_by(id_material_limpeza=form.material_limpeza_id.data,
                                     id_material_oclusao=form.material_oclusao_id.data,
                                     id_material_fixacao=form.material_fixacao_id.data,
                                     id_material_aplicacao=form.material_aplicacao_id.data).first():
        return {'descricao': 'Curativo não pode ser cadastrado.'}, status.HTTP_409_CONFLICT

    curativo_novo = CurativoModel(form.material_limpeza_id.data,
                                  form.material_oclusao_id.data,
                                  form.material_fixacao_id.data,
                                  form.material_aplicacao_id.data,
                                  form.frequencia_id.data)
    db.session.add(curativo_novo)
    db.session.commit()

    return {'descricao': 'Curativo cadastrado com sucesso.'}, status.HTTP_201_CREATED

@curativo.route("/curativos", methods=["GET"])
@login_required
@cache.cached(300)
@as_json
def listar_curativos():
    curativos = CurativoModel.query.all()

    if any(curativos):
        return {'descricao': [c.to_json() for c in curativos]}, status.HTTP_200_OK

    return {'descricao': 'Nenhum curativo encontrado.'}, status.HTTP_204_NO_CONTENT