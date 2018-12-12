from flask import Flask
import os


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('my_chat')
    #app.config.from_object(config[config_name])
    return app