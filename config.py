class Config(object):
    
    #Common configurations
    
    FLASK_CONFIG = "development"
    
    # Put any configurations here that are common across all environments
    SQLALCHEMY_DATABASE_URI = "sqlite:////db/touchlessAutomation.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #SECRET_KEY : A secret key that will be used for securely signing the session cookie 
    # and can be used for any other security related needs by extensions or your application. 
    # It should be a long random bytes or str. For example, copy the output of this to your config:
    # $ python -c 'import secrets; print(secrets.token_hex())' '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    SECRET_KEY = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'

    #SESSION_COOKIE_NAME : The name of the session cookie. Can be changed in case you already have a cookie with the same name.
    SESSION_COOKIE_NAME = 'session'

    #SESSION_COOKIE_DOMAIN: The domain match rule that the session cookie will be valid for. 
    # If not set, the cookie will be valid for all subdomains of SERVER_NAME. 
    # If False, the cookie’s domain will not be set.
    SESSION_COOKIE_DOMAIN = None

    #SESSION_COOKIE_PATH : The path that the session cookie will be valid for. If not set, 
    # the cookie will be valid underneath APPLICATION_ROOT or / if that is not set.
    SESSION_COOKIE_PATH = None

class DevelopmentConfig(Config):
    
    #Development configurations
    
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    FLASK_ENV = "development"
    FLASK_CONFIG = "development"
    PROPAGATE_EXCEPTIONS = True
    PRESERVE_CONTEXT_ON_EXCEPTION = True
    TRAP_HTTP_EXCEPTIONS = False

class ProductionConfig(Config):
    
    #Production configurations
    
    DEBUG = False
    TESTING = False
    FLASK_ENV = "production"
    FLASK_CONFIG = "production"
    PROPAGATE_EXCEPTIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TRAP_HTTP_EXCEPTIONS = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}