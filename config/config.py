class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "KLASLDAPOKPK33434KPOEQOK22LMqwe#!@#347447"

    SESSION_COOKIE_SECURE = True

    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = ''
    HOST = '127.0.0.1'
    PORT = 3306
    DATABASE = 'digital_leads_dados'
    CHARSET = 'utf8'

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    