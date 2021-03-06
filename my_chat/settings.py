
import os
import sys
from my_chat.task import send_message

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL',prefix + os.path.join(basedir,'data.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JOBS = [
        {
            'id':'job1',
            'func':send_message,
            'args':'',
            'trigger':'interval',
            'seconds':10
        }
    ]
    SCHEDULER_API_ENABLED = True


class DevelopmentConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URL = 'sqlite:///'
    WTF_CSRF_ENABLED = False

config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
}

