from flask import Blueprint, request, current_app
from flask.ext.api import status
from flask.ext.login import login_required, logout_user, login_user, current_user
from flask_json import as_json

from Src.Security import login_manager
from Src.Models import db
from Src.Forms.Conta.UsuarioAutenticacaoForm import UsuarioAutenticacaoForm
from Src.Forms.Conta.UsuarioForm import UsuarioForm
from Src.Models.Conta.UsuarioModel import UsuarioModel

conta = Blueprint('conta', __name__)


@login_manager.user_loader
def load_user(usuario_id):
    return UsuarioModel.query.filter(UsuarioModel.id == usuario_id).first()


@conta.route('/usuarios', methods=['POST'])
@as_json
def adicionar_usuario():
    form = UsuarioForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.senha.errors) or \
       any(form.nome.errors) or\
       any(form.email.errors):
        mensagem_erro = 'Usuário inválido. {0} {1} {2}'.format(
            ' '.join(form.senha.errors if form.senha.errors else ''),
            ' '.join(form.nome.errors if form.nome.errors else ''),
            ' '.join(form.email.errors if form.email.errors else ''))

        return {'descricao': mensagem_erro.strip()}, status.HTTP_400_BAD_REQUEST

    if UsuarioModel.query.filter_by(email=form.email.data).first() or\
       UsuarioModel.query.filter_by(nome=form.nome.data).first():
        return {'descricao': 'usuário não pode ser cadastrado.'}, status.HTTP_409_CONFLICT

    usuario_novo = UsuarioModel(form.nome.data, form.email.data, form.senha.data)
    db.session.add(usuario_novo)
    db.session.commit()

    return {'descricao':'Usuário cadastrado com sucesso.'}, status.HTTP_201_CREATED


@conta.route("/sessao", methods=["POST"])
@as_json
def autenticar():
    form = UsuarioAutenticacaoForm.from_json(request.get_json(force=True))
    form.validate_on_submit()

    if any(form.senha.errors) or\
       any(form.usuario.errors):
        mensagem_erro = 'Usuário inválido. {0} {1}'.format(
            ' '.join(form.senha.errors if form.senha.errors else ''),
            ' '.join(form.usuario.errors if form.usuario.errors else ''))

        return {'descricao': mensagem_erro.strip()}, status.HTTP_400_BAD_REQUEST

    usuario = UsuarioModel.query.filter_by(email=form.usuario.data).first()

    if usuario and usuario.senha_correta(form.senha.data):
        login_user(usuario)
        return {'descricao': 'Usuário autenticado com sucesso.'}, status.HTTP_200_OK

    return {'descricao': 'Usuário ou senha inválido.'}, status.HTTP_401_UNAUTHORIZED


@conta.route('/sessao', methods=["DELETE"])
@login_required
@as_json
def sair():
    logout_user()
    return {'descricao': 'Usuário desconectado com sucesso.'}, status.HTTP_200_OK


@conta.route('/sessao/usuario_info', methods=["GET"])
@login_required
@as_json
def checar_status():
    return {'autenticacao_status': current_user.to_json()}
