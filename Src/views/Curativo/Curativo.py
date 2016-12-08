from flask import Blueprint, jsonify
from flask.ext.api import status
from flask.ext.login import login_required

from Src import db
from Src.Forms.Curativo.Lesao import Lesao as LesaoForm
from Src.Forms.Curativo.Lesao import Lesao
from Src.Forms.Curativo.Procedimento import Procedimento as ProcedimentoForm
from Src.Models.Curativo.Procedimento import Procedimento
from Src.Forms.Curativo.Material import Material as MaterialForm
from Src.Models.Curativo.Material import Material
from Src.Forms.Curativo.Frequencia import Frequencia as FrequenciaForm
from Src.Models.Curativo.Frequencia import Frequencia
from Src.Forms.Curativo.ProcedimentoMaterialLista import ProcedimentoMaterialLista
from Src.Models.Curativo.ProcedimentoMaterial import ProcedimentoMaterial

curativo = Blueprint('curativo', __name__)


@curativo.route("/lesoes", methods=["POST"])
@login_required
def adicionar_lesao():
    form = LesaoForm()
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Lesão inválida. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return jsonify({'detalhe': mensagem_erro.strip()}), status.HTTP_400_BAD_REQUEST

    if not Lesao.query.filter_by(nome=form.nome.data).first():
        db.session.add(Lesao(form.nome.data))
        db.session.commit()

        return jsonify({'detalhe': 'Lesão cadastrada com sucesso.'}), status.HTTP_201_CREATED

    return jsonify({'detalhe': 'Impossível cadastrar a lesão.'}), status.HTTP_409_CONFLICT


@curativo.route("/lesoes", methods=["GET"])
@login_required
def listar_lesoes():
    lesoes = Lesao.query.all()

    if any(lesoes):
        return jsonify({'detalhe': [l.to_json() for l in lesoes]}), status.HTTP_200_OK

    return jsonify({'detalhe': 'Nenhuma lesão encontrada.'}), status.HTTP_204_NO_CONTENT


@curativo.route("/materiais", methods=["POST"])
@login_required
def adicionar_material():
    form = MaterialForm()
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Material inválido. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return jsonify({'detalhe': mensagem_erro.strip()}), status.HTTP_400_BAD_REQUEST

    if not Material.query.filter_by(nome=form.nome.data).first():
        db.session.add(Material(form.nome.data))
        db.session.commit()

        return jsonify({'detalhe': 'Material cadastrado com sucesso.'}), status.HTTP_201_CREATED

    return jsonify({'detalhe': 'Impossível cadastrar o material.'}), status.HTTP_409_CONFLICT


@curativo.route("/materiais", methods=["GET"])
@login_required
def listar_materiais():
    materiais = Material.query.all()

    if any(materiais):
        return jsonify({'detalhe': [m.to_json() for m in materiais]}), status.HTTP_200_OK

    return jsonify({'detalhe': 'Nenhum material encontrado.'}), status.HTTP_204_NO_CONTENT


@curativo.route("/procedimentos", methods=["POST"])
@login_required
def adicionar_procedimento():
    form = ProcedimentoForm()
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Procedimento inválido. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return jsonify({'detalhe': mensagem_erro.strip()}), status.HTTP_400_BAD_REQUEST

    if not Procedimento.query.filter_by(nome=form.nome.data).first():
        db.session.add(Procedimento(form.nome.data))
        db.session.commit()

        return jsonify({'detalhe': 'Procedimento cadastrado com sucesso.'}), status.HTTP_201_CREATED

    return jsonify({'detalhe': 'Impossível cadastrar o procedimento.'}), status.HTTP_409_CONFLICT


@curativo.route("/procedimentos", methods=["GET"])
@login_required
def listar_procedimentos():
    procedimentos = Procedimento.query.all()

    if any(procedimentos):
        return jsonify({'detalhe': [p.to_json() for p in procedimentos]}), status.HTTP_200_OK

    return jsonify({'detalhe': 'Nenhum procedimento encontrado.'}), status.HTTP_204_NO_CONTENT


@curativo.route("/freq_curativos", methods=["POST"])
#@login_required
def adicionar_frequencia():
    form = FrequenciaForm()
    form.validate_on_submit()

    if any(form.nome.errors):
        mensagem_erro = 'Frequência de curativo inválida. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return jsonify({'detalhe': mensagem_erro.strip()}), status.HTTP_400_BAD_REQUEST

    if not Procedimento.query.filter_by(nome=form.nome.data).first():
        db.session.add(Procedimento(form.nome.data))
        db.session.commit()

        return jsonify({'detalhe': 'Frequência de curativo cadastrado com sucesso.'}), status.HTTP_201_CREATED

    return jsonify({'detalhe': 'Impossível cadastrar a frequência de curativo.'}), status.HTTP_409_CONFLICT


@curativo.route("/freq_curativos", methods=["GET"])
#@login_required
def listar_frequencia():
    frequencias = Frequencia.query.all()

    if any(frequencias):
        return jsonify({'detalhe': [f.to_json() for f in frequencias]}), status.HTTP_200_OK

    return jsonify({'detalhe': 'Nenhuma frequência de curativo encontrada.'}), status.HTTP_204_NO_CONTENT


@curativo.route("/procedimentos/materiais", methods=["POST"])
#@login_required
def adicionar_procedimento_material():
    form = ProcedimentoMaterialLista()
    form.validate_on_submit()

    if any(form.procedimento_materiais.errors):
        mensagem_erro = 'Materiais ou Procedimentos inválidos. {0}'.format(
            ' '.join(form.nome.errors if form.nome.errors else ''))

        return jsonify({'detalhe': mensagem_erro.strip()}), status.HTTP_400_BAD_REQUEST

    #bulk_save_objects
    if not ProcedimentoMaterial.query.filter_by(nome=form.nome.data).first():
        db.session.add(Procedimento(form.nome.data))
        db.session.commit()

        return jsonify({'detalhe': 'Frequência de curativo cadastrado com sucesso.'}), status.HTTP_201_CREATED

    return jsonify({'detalhe': 'Impossível cadastrar a frequência de curativo.'}), status.HTTP_409_CONFLICT