from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_json import FlaskJSON
import wtforms_json

app = Flask(__name__)

FlaskJSON(app)

app.secret_key = 'secret'
app.config.update({'SQLALCHEMY_DATABASE_URI': 'sqlite:///Data/ferida.db',})
app.config["WTF_CSRF_ENABLED"] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

with app.test_request_context():
    from Src.Models.Autenticacao import Usuario
    from Src.Views.Autenticacao.Autenticacao import autenticacao
    from Src.Views.Curativo.Curativo import  curativo

    app.register_blueprint(autenticacao, url_prefix='/api/v1')
    app.register_blueprint(curativo, url_prefix='/api/v1')

    wtforms_json.init()
    db.create_all()

