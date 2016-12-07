 from Src.main import app, db

 with app.test_request_context():
        from Src.App.Autenticacao import PapeisUsuario, Papel, Usuario

        db.create_all()