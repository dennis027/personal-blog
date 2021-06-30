import os
class Config:
    """
    general config parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #email configutions
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    """
    prod config child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
class DevConfig(Config):
    """
    dev config child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    DEBUG = True

config_options={
    'development':DevConfig,
    'production' :ProdConfig
}    

    