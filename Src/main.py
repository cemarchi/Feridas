from Src import app


@app.route('/api/v1')
def index():
    return 'Serviço Web de atendimento de feridas está em execução!'


if __name__ == '__main__':
    app.run('localhost', 5000, debug=True, use_reloader=False)
