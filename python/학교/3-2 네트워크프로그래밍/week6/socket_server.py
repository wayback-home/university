import socket
import struct
import threading
import time


class ChatService:
    def __int__(self, sock):
        self.sock = sock
        self.done = False
        self.rcvd_th = None
        self.snd_th = None

    def go(self):
        self.rcvd_th = threading.Thread(target=self.rcvd_fn)
        self.snd_th = threading.Thread(target=self.snd_fn)
        self.rcvd_th.start()
        self.snd_th.start()
        self.rcvd_th.join()
        self.snd_th.join()

        print("client closed")

    def snd_fn(self):
        count = 0
        while not self.done:
            count += 1
            self.sock.send(struct.pack(">I", count))
            time.sleep(2)
        self.sock.close()

    def rcvd_fn(self):
        self.sock.settimeout(2)
        while not self.done:
            try:
                buf = self.sock.recv(1024)
                if buf.decode() == "exit":
                    self.done = True
                else:
                    print(buf.decode())
            except socket.timeout:
                pass


SERVER_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", SERVER_PORT))
sock.listen(5)

while True:
    print("Waiting connection request")
    cli_sock, _ = sock.accept()
    client = ChatService(cli_sock)
    client.go()
    break

sock.close()
