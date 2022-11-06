import socket
import struct

ip_addr = struct.pack('>4B', 192, 168, 0, 1)
print(socket.inet_ntoa(ip_addr))




print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname('www.ut.ac.kr'))
print(socket.inet_aton('192.168.0.1'))
print(socket.inet_ntoa(b'\xc0\xa8\x00\x01'))