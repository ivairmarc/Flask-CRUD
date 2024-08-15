from app.app import create_app
from app.database import init_db


app = create_app()

# Cria as tabelas no banco de dados
with app.app_context():
    init_db()


if __name__ == '__main__':
    app.run()