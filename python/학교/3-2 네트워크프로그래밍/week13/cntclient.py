import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 9999))


while True:
    buf = sock.recv(1024)
    if len(buf) == 0:
        break
    else:
        print(buf.decode())

sock.close()
