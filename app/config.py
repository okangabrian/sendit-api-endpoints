class Config(object):
	"""docstring for Config"""
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG=True
    TESTING=False

class TestingConfig(Config):
    DEBUG=True
    TESTING=True

app_config={
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "default":DevelopmentConfig
}
