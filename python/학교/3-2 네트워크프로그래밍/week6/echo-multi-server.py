import socket
import struct
import threading

def eserv(*arg):
    cli_sock = arg[0]

    while True:
        data = cli_sock.recv(1024)
        if data.decode() == 'exit':
            break
        print(data.decode())
        cli_sock.send(data)

    cli_sock.close()

SERVER_PORT = 9998

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', SERVER_PORT))
sock.listen(5)
sock.settimeout(5)
done = False
while not done:
    try:
        try:
            cli_sock, _ = sock.accept()
            print('connected')

            ec = threading.Thread(target=eserv, args=(cli_sock,))
            ec.start()


        except socket.timeout:
            print('time out')
    except KeyboardInterrupt:
        print('ctrl-C')
        done = True
sock.close()