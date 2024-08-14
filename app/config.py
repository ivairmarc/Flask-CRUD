class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "KLASLDAPOKPK33434KPOEQOK22LMqwe#!@#347447"

    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    