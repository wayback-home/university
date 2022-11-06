import socket
import threading

cli_list = []

def chat_service(*arg):
    csock = arg[0]
    while True:
        buf = csock.recv(1024)
        print(buf.decode())
        if buf.decode() == 'exit':
            cli_list.remove(csock)
            break
        else:
            # csock.send(buf)
            for s in cli_list:
                s.send(buf)

    csock.close()

SERVER_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', SERVER_PORT))
sock.listen(5)
sock.settimeout(4)
while True:
    try:
        try:
            cli_sock, cli_addr = sock.accept()

            cli_list.append(cli_sock)

            cli_th = threading.Thread(target=chat_service,args=(cli_sock,))
            cli_th.start()
        except socket.timeout:
            print('timeout.')
            pass
    except KeyboardInterrupt:
        print('^C is pressed.')
        break

sock.close()