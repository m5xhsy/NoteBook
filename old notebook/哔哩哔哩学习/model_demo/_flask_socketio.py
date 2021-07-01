from flask import Flask, render_template
from flask_socketio import SocketIO
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('connect')
def connect():
    print('connection established')


@socketio.on('my_event')
def handle_json(json):
    print('received json: ' + str(json))


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app,debug=True)