import os

# from dotenv import load_dotenv

# load_dotenv(dotenv_path='.env')


class Config(object):
    """Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'somesecretkey')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'


class DevelopmentConfig(Config):
    """Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """Production configurations
    """

    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configurations
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}