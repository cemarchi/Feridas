from flask import Flask
from flask_json import FlaskJSON
import wtforms_json

from .Config import configure_app
from .Cache import cache
from .Models import db
from .Security import login_manager
from Src.Controllers.Conta.Conta import conta
from Src.Controllers.Curativo.Curativo import curativo

app = Flask(__name__)

FlaskJSON(app)

configure_app(app, 'development')
cache.init_app(app)
db.init_app(app)
login_manager.init_app(app)
wtforms_json.init()

app.register_blueprint(conta, url_prefix='/api/v1')
app.register_blueprint(curativo, url_prefix='/api/v1')

with app.test_request_context():
    from Src.Models.Conta import UsuarioModel
    from Src.Models.Curativo import CurativoModel, FrequenciaModel, LesaoModel, MaterialModel, \
        ProcedimentoMaterialModel, ProcedimentoModel

    db.create_all()
