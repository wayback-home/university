import socket
import threading
import time
import struct

class ChatService:
    def __init__(self, sock):
        self.sock = sock
        self.r_th = None
        self.s_th = None
        self.done = False

    def go(self):
        self.r_th = threading.Thread(target=self.r_fn)
        self.s_th = threading.Thread(target=self.s_fn)
        self.r_th.start()
        self.s_th.start()
        self.r_th.join()
        self.s_th.join()
        self.sock.close()

    def r_fn(self):
        while not self.done:
            data = self.sock.recv(2048)
            strdata = data.decode()
            if strdata == 'exit':
                self.done = True
            else:
                print(strdata)

    def s_fn(self):
        count = 0
        while not self.done:
            count += 1
            self.sock.send(struct.pack('>I', count))
            time.sleep(2)

def conproc(*arg):
    cs = ChatService(arg[0])
    cs.go()

SERVER_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', SERVER_PORT))
sock.listen(5)
sock.settimeout(4)
while True:
    try:
        try:
            cli_sock, _ = sock.accept()
            ccm = threading.Thread(target=conproc, args=(cli_sock,))
            ccm.start()
        except socket.timeout:
            print('timeout..')
    except KeyboardInterrupt:
        print('^C')
        break

sock.close()

