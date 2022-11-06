import socket
import struct

SERVER_PORT = 9998

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", SERVER_PORT))
sock.listen(5)
sock.settimeout(5)
done = False
while not done:
    try:
        try:
            cli_sock, _ = sock.accept()
            print("connected")
            data = cli_sock.recv(2048)
            print(data.decode())
            print(struct.unpack(">f", data)[0])
            cli_sock.send(data)
            cli_sock.close()
            done = True
        except socket.timeout:
            print("time out")
    except KeyboardInterrupt:
        print("ctrl-C")
        done = True
sock.close()
