# Remoto de Atendimento de Feridas

Endpoints
=============================================

Endpoint: 'http://localhota:5000/api/v1/usuarios'

   POST:  cadastra um enfermeiro
   Exemplo JSON: {
                    "nome": "claudia",
                    "email": "c@aol.com.br",
                    "senha":"12345"
                 }



{
    "usuario": "c@aol.com.br",
  	"senha":"12345"
}

{
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
