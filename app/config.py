import os


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = "\xeb\x15\xbfk\xa2\xe0|\xd1P\xa5\x96\x12\xb0)\xa0\x14\xe7,\xad\xc7L\xd3\x93]"

    SESSION_COOKIE_SECURE = True

    

class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    