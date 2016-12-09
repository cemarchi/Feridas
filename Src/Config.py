import logging


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'

    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s\nArquivo: %(filename)s'\
                     '\nMétodo: %(funcName)s\nMensagem: %(message)s\n'
    LOGGING_LOCATION = 'Log/ferida.log'
    LOGGING_LEVEL = logging.DEBUG

    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Database/ferida.db'
    SECRET_KEY = 'secret'


config = {
    "development": "Config.DevelopmentConfig"
}


def configure_app(app, config_type):
    app.config.from_object(config[config_type])

    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
