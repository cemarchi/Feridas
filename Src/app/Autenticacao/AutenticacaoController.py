from flask import Response, request, abort, jsonify
from flask.ext.login import login_required

from Src.App.Autenticacao import auth
from Src.App.Autenticacao.Usuario import Usuario
from Src.Main import db


@auth.route('/usuarios', methods=['POST'])
def new_user():
    nome = request.json.get('nome')
    email = request.json.get('email')
    senha = request.json.get('senha')

    if email is None or senha is None:
        abort(400)
    if Usuario.query.filter_by(email=email).first() is not None:
        abort(400)

    usuario = Usuario(nome, email, senha)
    db.session.add(usuario)
    db.session.commit()

    return (jsonify({'usuario': usuario.email}), 201,
            {'Location': url_for('obter_usuario', id=usuario.id, _external=True)})


@auth.route('/usuarios/<int:id>', methods=['GET'])
def obter_usuario(id):
    usuario = 10

    if not usuario:
        abort(400)

    return jsonify({'usuario': usuario.email})


@auth.route("/", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        #username = request.form['username']
        #password = request.form['password']
        #if password == username + "_secret":
            #id = username.split('user')[1]
            #user = User(id)
            #login_user(user)
            #return redirect(request.args.get("next"))
        #else:
        return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


@auth.route("/logout")
@login_required
def logout():
    return Response('<p>Logged out</p>')
