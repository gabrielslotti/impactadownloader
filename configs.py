class BaseConfig(object):
    '''Base config class'''
    DEBUG = True
    TESTING = False

    SECRET_KEY = b'secret'

    FACEBOOK_CLIENT_ID = '276672413508240'
    FACEBOOK_CLIENT_SECRET = '81b5bbccc39a83cf08ba09d8d45bf069'

    GITHUB_CLIENT_ID = ''
    GITHUB_CLIENT_SECRET = ''

class ProductionConfig(BaseConfig):
    '''Production specific config'''
    DEBUG = False
    
class DevelopmentConfig(BaseConfig):
    '''Development environment specific configuration'''
    DEBUG = True
    TESTING = True