# 서버 -> 클라이언트
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 8080))
sock.listen(1)

connectionSock, addr = sock.accept()

filename = connectionSock.recv(1024)
data_transferred = 0


with open(filename, "rb") as fd:
    data = fd.read(1024)
    while data:
        data_transferred += connectionSock.send(data)
        data = fd.read(1024)

sock.close()

# 서버 <- 클라이언트
# import socket
# import threading

# def cli_comm(*arg):
#     csock = arg[0]
#     buf = csock.recv(4096)
#     fd = open("data.rcv", "wb")
#     fd.write(buf)
#     fd.close()
#     csock.close()

# SERVER_PORT = 9998

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(("", SERVER_PORT))
# sock.listen(5)
# cli_sock, _ = sock.accept()
# th = threading.Thread(target=cli_comm, args=(cli_sock,))
# th.start()
# th.join()
# sock.close()
