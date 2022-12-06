from scapy.all import *
from scapy.layers.inet import Ether, IP, TCP, UDP, ICMP
from scapy.packet import Raw

ether = Ether()
ip = IP()
tcp = TCP()
raw = Raw()
udp = UDP()
icmp = ICMP()
raw.load = b"hello"

ip.dst = "210.119.145.6"
udp.sport = 9999  # 보내는거
udp.dport = 12345  # 수신

packet = ether / ip / udp / icmp / raw

packet.show()
sr1(packet)
