from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_apscheduler import APScheduler

db = SQLAlchemy()
login_manager = LoginManager()
socketio = SocketIO()
scheduler = APScheduler()