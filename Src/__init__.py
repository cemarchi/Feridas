from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = 'secret'
app.config.update({'SQLALCHEMY_DATABASE_URI': 'sqlite:///Data/ferida.db',})

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'autenticacao/entrar'

with app.test_request_context():
    from Src.Models.Autenticacao import Usuario
    from Src.Views.Autenticacao.Autenticacao import autenticacao

    app.register_blueprint(autenticacao, url_prefix='/api/v1')
    db.create_all()

