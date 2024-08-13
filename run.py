from app.app import create_app, db

app = create_app()

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
