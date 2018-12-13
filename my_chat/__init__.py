from flask import Flask
import os
from my_chat.blueprints.auth import auth_bp
from my_chat.blueprints.chat import chat_bp
from my_chat.settings import config
from my_chat.extensions import db,socketio
import click
# from my_chat.models import User,Message



def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app = Flask('my_chat')
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_command(app)

    return app


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)

def register_extensions(app):
    db.init_app(app)
    socketio.init_app(app)

def register_command(app):
    @app.cli.command()
    def cdb():
        click.echo('Initializing the database...')
        db.drop_all()
        db.create_all()
        click.echo('Done')
