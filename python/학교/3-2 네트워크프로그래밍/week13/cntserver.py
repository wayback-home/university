import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 9999))
sock.listen(5)

cli_sock, _ = sock.accept()

count = 0
try:
    while True:
        count += 1
        cli_sock.send(str(count).encode())
        time.sleep(5)
except KeyboardInterrupt:
    cli_sock.close()

sock.close()
