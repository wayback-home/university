import socket
import threading


def cli_comm(*arg):
    csock = arg[0]
    buf = csock.recv(4096)
    fd = open("data.rcv", "wb")
    fd.write(buf)
    fd.close()
    csock.close()


SERVER_PORT = 9998

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", SERVER_PORT))
sock.listen(5)
cli_sock, _ = sock.accept()
th = threading.Thread(target=cli_comm, args=(cli_sock,))
th.start()
th.join()
sock.close()
