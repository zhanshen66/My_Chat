from flask import Blueprint
from my_chat.extensions import socketio
from flask import render_template
from flask_socketio import emit


chat_bp = Blueprint('chat',__name__)


@socketio.on('new message')
def new_message(message_body):
    print(message_body)
    emit('new message',{'message':message_body['talk_words'],'my_id':message_body["my_id"]},broadcast=True)




@chat_bp.route('/')
def index():
    return render_template('simplechat.html')


