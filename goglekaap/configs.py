
class Config:
    """Flask Config"""
    SECRET_KEY = 'secret key'
    SESSION_COOKIE_NAME = 'goglekaap'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3308/goglekaap?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'

class DevelopmentConfig(Config):
    """Flask Config for dev"""
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    #TODO Front 호출 시 처리
    WTF_CSRF_ENABLED = False


class ProductionConfig(DevelopmentConfig):
    """Production"""
    pass