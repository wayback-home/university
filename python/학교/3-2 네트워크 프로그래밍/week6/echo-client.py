import socket
import time

SERVER_PORT = 9998
SERVER_IP = socket.gethostbyname(socket.gethostname())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

sock.send('좋은 아침'.encode())
data = sock.recv(2048)
print(data.decode())

sock.close()