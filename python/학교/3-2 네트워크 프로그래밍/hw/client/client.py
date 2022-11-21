# 서버 -> 클라이언트
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8080))

filename = sys.stdin.readline().strip()
sock.sendall(filename.encode("utf-8"))

data = sock.recv(1024)
data_transferred = 0


with open("data.rcv", "wb") as fd:
    while data:
        fd.write(data)
        data_transferred += len(data)
        data = sock.recv(1024)

sock.close()


# 서버 <- 클라이언트
# import socket
# import sys

# SERVER_PORT = 9998
# SERVER_IP = socket.gethostbyname(socket.gethostname())

# filename = sys.stdin.readline().strip()
# fd = open(filename, "rb")

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((SERVER_IP, SERVER_PORT))

# buf = fd.read(4096)
# sock.send(buf)

# fd.close()
# sock.close()
