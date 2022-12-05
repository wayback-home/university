import socket
import struct
import threading

class ChatClient:
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

    def r_fn(self):
        self.sock.settimeout(3)
        while not self.done:
            try:
                data = self.sock.recv(1024)
                try:
                    print(struct.unpack('>I', data)[0])
                except struct.error:
                    pass
            except socket.timeout:
                pass

    def s_fn(self):
        while not self.done:
            data = input('> ')
            self.sock.send(data.encode())
            if data == 'exit':
                self.done = True


SERVER_PORT = 9999
SERVER_IP = socket.gethostbyname(socket.gethostname())

print(SERVER_IP)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((SERVER_IP, SERVER_PORT))

cc = ChatClient(sock)
cc.go()

sock.close()