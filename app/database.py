from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import Config


conf = Config()
# Construir a string de conexão
connection_string = f'{conf.DIALECT}+{conf.DRIVER}://{conf.USERNAME}:{conf.PASSWORD}@{conf.HOST}:{str(conf.PORT)}/{conf.DATABASE}?charset={conf.CHARSET}'

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
    import app.models
    Base.metadata.create_all(bind=engine)
    