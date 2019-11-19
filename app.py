from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import websocket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		return render_template('home.html')
	else:
		return render_template('home.html')

@socketio.on('message')
def handleMessage(msg):
	print('message: ' + msg)
	ws = websocket.create_connection("ws://localhost:9443/socket_test")
	ws.send(msg)
	result =  ws.recv()
	ws.close()
	send(result,broadcast=True)


if __name__ == '__main__':
	socketio.run(app,debug=True,host='0.0.0.0',port=8000)