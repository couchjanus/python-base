# Client TCP srv06_client.py

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 53000        # Port to listen on (non-privileged ports are > 1023)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.sendall(b'Hello, world')
data = client.recv(1024)
client.close()
print('Received', repr(data))

# python srv06_client.py 
# Received b'Hello, world'
