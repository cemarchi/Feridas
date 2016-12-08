from flask import Blueprint, jsonify
from flask.ext.api import status
from flask.ext.login import login_required, logout_user, login_user, current_user

from Src import login_manager, db
from Src.Forms.Autenticacao.UsuarioAutenticacao import UsuarioAutenticacao
from Src.Forms.Autenticacao.Usuario import Usuario as UsuarioNovo
from Src.Models.Autenticacao.Usuario import Usuario

autenticacao = Blueprint('autenticacao', __name__)


@login_manager.user_loader
def load_user(usuario_id):
    return Usuario.query.filter(Usuario.id == usuario_id).first()


@autenticacao.route('/usuarios', methods=['POST'])
def adicionar_usuario():
    form = UsuarioNovo()
    form.validate_on_submit()

    if any(form.senha.errors) or \
       any(form.nome.errors) or\
       any(form.email.errors):
        mensagem_erro = 'Usuário inválido. {0} {1} {2}'.format(
            ' '.join(form.senha.errors if form.senha.errors else ''),
            ' '.join(form.nome.errors if form.nome.errors else ''),
            ' '.join(form.email.errors if form.email.errors else ''))

        return jsonify({'detalhe': mensagem_erro.strip()}), status.HTTP_400_BAD_REQUEST

    if Usuario.query.filter_by(email=form.email.data).first() or\
       Usuario.query.filter_by(nome=form.nome.data).first():
        return jsonify({'detalhe': 'usuário não pode ser cadastrado.'}), status.HTTP_409_CONFLICT

    usuario_novo = Usuario(form.nome.data, form.email.data, form.senha.data)
    db.session.add(usuario_novo)
    db.session.commit()

    return jsonify({'detalhe': 'usuário cadastrado com sucesso.'}), status.HTTP_201_CREATED


@autenticacao.route("/sessao", methods=["POST"])
def autenticar():
    form = UsuarioAutenticacao()
    form.validate_on_submit()

    if any(form.senha.errors) or\
       any(form.usuario.errors):
        mensagem_erro = 'Usuário inválido. {0} {1}'.format(
            ' '.join(form.senha.errors if form.senha.errors else ''),
            ' '.join(form.usuario.errors if form.usuario.errors else ''))

        return jsonify({'detalhe': mensagem_erro.strip()}), status.HTTP_400_BAD_REQUEST

    usuario = Usuario.query.filter_by(email=form.usuario.data).first()

    if usuario and usuario.senha_correta(form.senha.data):
        login_user(usuario)
        return jsonify({'detalhe': 'Usuário autenticado com sucesso.'}), status.HTTP_200_OK

    return jsonify({'detalhe': 'Usuário ou senha inválido.'}), status.HTTP_401_UNAUTHORIZED


@autenticacao.route('/sessao', methods=["DELETE"])
@login_required
def sair():
    logout_user()
    return jsonify({'detalhe': 'Usuário desconectado com sucesso.'}), status.HTTP_200_OK


@autenticacao.route('/sessao', methods=["GET"])
@login_required
def checar_status():
    return jsonify({'autenticacao_status': current_user.to_json()})
