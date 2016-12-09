import traceback
from flask import request, jsonify
from flask.ext.api import status

from Src import app


@app.route('/api/v1')
def index():
    return 'Serviço Web de atendimento de feridas está em execução!'


@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    app.logger.error('%s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', request.remote_addr, request.method, request.scheme,
                     request.full_path, tb)
    return jsonify({'mensagem_erro': 'Falha no serviço web. Se o problema persistir, por favor entrar em contato conosco.'}), \
           status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True, use_reloader=False)
