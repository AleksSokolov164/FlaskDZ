class Config(object):
    USER = ''
    PASSWORD = ''
    HOST = ''
    PORT = ''
    DB = ''

    SQLALCHEMY_DATABASE_URI = f'sqlite:///newflask.db'
    SECRET_KEY = 'jhgfjiunmbgfhglk9hlh6767khghckil90'
    SQLALCHEMY_TRACK_MODIFICATIONS = True