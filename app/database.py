from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os


load_dotenv()

# Construir a string de conexão
connection_string = os.getenv('DATABASE_URI', '')

# Configurar o SQLAlchemy
engine = create_engine(connection_string, echo=False, pool_size=20, max_overflow=0)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import app.leads.leads_model
    import app.users.user_model
    import app.commercial.commercial_model
    import app.groups.group_model
    import app.product.product_model

    from .create_database import create_db
    create_db()
    Base.metadata.create_all(bind=engine)
    