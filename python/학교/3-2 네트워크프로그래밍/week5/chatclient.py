import socket
import threading

done = False

def snd_fn(*arg):
    global  done
    sock = arg[0]
    while not done:
        buf = input('> ')
        sock.send(buf.encode())
        if buf == 'exit':
            done = True

def rcv_fn(*arg):
    sock = arg[0]
    sock.settimeout(2)
    while not done:
        try:
            buf = sock.recv(1024)
            if buf is not None and len(buf) > 0:
                print(buf.decode())
            else:
                break
        except socket.timeout:
            pass

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

snd_th = threading.Thread(target=snd_fn, args=(sock,))
rcv_th = threading.Thread(target=rcv_fn, args=(sock,))

snd_th.start()
rcv_th.start()

snd_th.join()
rcv_th.join()

sock.close()