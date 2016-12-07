from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'secret'
app.config.update({'SQLALCHEMY_DATABASE_URI': 'sqlite:///db/ferida.db',})
db = SQLAlchemy(app)


@app.route('/api/v1')
def index():
    return 'Serviço Web de atendimento de feridas está em execução!'


if __name__ == '__main__':
    app.run(debug=True)
