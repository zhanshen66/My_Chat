from flask import Flask
import os
from my_chat.blueprints.auth import auth_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('my_chat')
    #app.config.from_object(config[config_name])
    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(auth_bp)