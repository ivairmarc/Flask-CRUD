class Config:
    user = 'root'
    password = 'comspirace'
    database_db = 'user_db'
    host = 'localhost'

    SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{password}@{host}/{database_db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
