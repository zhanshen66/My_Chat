from flask import Flask


def create_app():
    app = Flask('my_chat')
    return app