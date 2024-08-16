from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os


load_dotenv()

# Construir a string de conexão
connection_string = os.getenv('DATABASE_URI', '')

# Configurar o SQLAlchemy
engine = create_engine(connection_string, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import database.models.leads_model
    import database.models.user_model
    import database.models.commercial_model
    import database.models.group_model
    import database.models.product_model


    Base.metadata.create_all(bind=engine)
    