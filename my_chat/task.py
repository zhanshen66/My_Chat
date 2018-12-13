
from flask_socketio import emit

def send_message():
    print('执行定时任务')
    # emit('new message', {'message': '广播消息', 'my_id': 0}, broadcast=True)
