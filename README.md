# Remoto de Atendimento de Feridas

#INICIAR O SERVIÇO

Console windows: navegar até o diretório onde encontra-se o arquivo Main.py

Inserir os seguintes comandos:

SET FLASK_APP=Main.py
flask run

ou

python -m flask run

Linux:

$ export FLASK_APP=Main.py
$ flask run

ou

$ python -m flask run


Endpoints
=============================================

Endpoint: 'http://localhota:5000/api/v1/usuarios'

   POST:  cadastra um enfermeiro.
   Exemplo JSON: {
                    "nome": "claudia",
                    "email": "c@aol.com.br",
                    "senha":"12345"
                 }

Endpoint: 'http://localhota:5000/api/v1/sessao'

   POST:  autentica um enfermeiro.
   Exemplo JSON: {
                    "usuario": "c@aol.com.br",
                    "senha":"12345"
                 }

   DELETE:  enfermeiro não está mais autenticado. Exige enfermeiro autenticado

Endpoint: 'http://localhota:5000/api/v1/sessao/usuario_info'

    GET:  obtém informação do enfermeiro autenticado. Exige enfermeiro autenticado.

Endpoint: 'http://localhota:5000/api/v1/sessao/usuario_info'

    POST:  cadastra uma lesão. Exige enfermeiro autenticado.
    Exemplo JSON: { "nome": "Lesão por pressão"}

    GET:  obtém todas as lesões cadastradas. Exige enfermeiro autenticado.

Endpoint: 'http://localhota:5000/api/v1/materiais'

    POST:  cadastra uma material. Exige enfermeiro autenticado
    Exemplo JSON: { "nome": "Hipergel"}

    GET:  obtém todos os materiais cadastrados. Exige enfermeiro autenticado.

Endpoint: 'http://localhota:5000/api/v1/procedimentos'

    POST:  cadastra um procedimento. Exige enfermeiro autenticado
    Exemplo JSON: { "nome": "Aplicação"}

    GET:  obtém todos os procedimentos cadastrados. Exige enfermeiro autenticado.

Endpoint: 'http://localhota:5000/api/v1/procedimentos/materiais'

    POST:  cadastra vários procedimentos com seus respectivos materiais associados. Exige enfermeiro autenticado
    Exemplo JSON: {
                    "procedimentos_materiais": [
                            {
                                "procedimento_id": 1,
                                "material_id": 2
                            },
                            {
                                "procedimento_id": 2,
                                "material_id": 3
                            },
                            {
                                "procedimento_id": 2,
                                "material_id": 1
                            },
                            {
                                "procedimento_id": 3,
                                "material_id": 4
                            }
                        ]
                    }

    GET:  obtém todos os procedimentos e materiais cadastrados. Exige enfermeiro autenticado.

Endpoint: 'http://localhota:5000/api/v1/freq_curativos'

    POST:  cadastra uma frequência do curativo. Exige enfermeiro autenticado
    Exemplo JSON: { "nome": "12 em 12 horas"}

    GET:  obtém todas as frequências cadastradas. Exige enfermeiro autenticado.

Endpoint: 'http://localhota:5000/api/v1/curativos'

    POST:  cadastra um curativo. Exige enfermeiro autenticado
    Exemplo JSON: {
                      "material_limpeza_id": 1,
                      "material_oclusao_id": 2,
                      "material_fixacao_id": 3,
                      "material_aplicacao_id": 4,
                      "frequencia_id": 1
                  }

    GET:  obtém todos os curativos cadastradas. Exige enfermeiro autenticado.

