import os


class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = 'certifiedgirltoto'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'


class ProdConfig(Config):
    """
    Production configuration
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}