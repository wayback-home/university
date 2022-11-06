import socket
import sys

SERVER_PORT = 9998
SERVER_IP = socket.gethostbyname(socket.gethostname())

if len(sys.argv) < 2:
    print("usage : python fileclient.py filename")
    exit(0)

fd = open(sys.argv[1], "rb")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

buf = fd.read(4096)
sock.send(buf)

fd.close()
sock.close()
