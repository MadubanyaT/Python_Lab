import socketio

# implementing a client that connects to the server

sio = socketio.Client() # connecting to the sever

@sio.event
def connect():
    print("Connection established")

@sio.event
def disconnect():
    print("disconnected from server")

sio.connect('http://localhost:8080')
#sio.emit('index', 'Tshepho')
sio.emit('message', {'data': 'my data'}) # emitting data (dict) to the server (print_message)
sio.wait()


