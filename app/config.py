import os
from configparser import ConfigParser


class BaseConfig(object):
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SECRET_KEY = "justincase"


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test_db."""
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/test_db'
    TESTING = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """
    DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/stackoverlite'
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
