from flask import Blueprint
from my_chat.extensions import socketio
from flask import render_template
from flask_socketio import emit
from threading import Lock



chat_bp = Blueprint('chat',__name__)

thread = None
thread_lock = Lock()


@socketio.on('new message')
def new_message(message_body):
    print(message_body)
    emit('new message',{'message':message_body['talk_words'],'my_id':message_body["my_id"]},broadcast=True)

def background_thread():
    while True:
        socketio.sleep(1)
        print('send message')
        socketio.emit('system message', {'message': '广播消息', 'my_id': 0})

@socketio.on('connect')
def connect():
    print('in connect')
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target = background_thread)





@chat_bp.route('/')
def index():
    return render_template('simplechat.html')


