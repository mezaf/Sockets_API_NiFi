import websocket
from websocket import create_connection
ws = create_connection("ws://localhost:9443/socket_test")
print("Sending 'Hello, World'...")
ws.send("Hello, Worlds")
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()