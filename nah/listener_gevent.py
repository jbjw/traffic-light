# using socket.io

# from socketIO_client import SocketIO, LoggingNamespace

# import socketIO_client
from socketIO_client import SocketIO

socket = SocketIO( 'localhost', 80 )
socket.send('blah')
socket.emit('message', 'blah')


# import websocket as ws

# socket = websocket.create_connection("ws://echo.websocket.org/")
socket = websocket.create_connection("ws://localhost/")
socket.send("Hello, World")
result = socket.recv()
print(result)
socket.close()
