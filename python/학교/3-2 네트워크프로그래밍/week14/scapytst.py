from scapy.all import *


# def pktview(p):
#     p.show()


# sniff(prn=pktview, count=2, filter="tcp")

# ! scapytst.py
# def pktview(p):
#     p[2].show()


# pktinfo = sniff(prn=pktview, count=2, filter="tcp", store=True)
# wrpcap("abc.pcap", pktinfo)  # 캡처, 확장자 노상관


# ! scapytst.py(터미널 3개필요, cntserver, scapy, cntclient)
# def pktview(p):
#     # p[2].show()
#     appdata = p.getlayer("Raw")
#     print(appdata.load)


# pktinfo = sniff(prn=pktview, filter="tcp port 9999")
# wrpcap("abc.pcap", pktinfo)  # 캡처, 확장자 노상관

# ! scapytst.py
def pktview(p):
    # p[2].show()
    segment = p.getlayer("TCP")
    if segment.sport == 9999:
        appdata = p.getlayer("Raw")
        if appdata:
            print(appdata.load)


iflist = get_if_list()
scapy_if = conf.iface
print(scapy_if)


for interface in iflist:
    if "loopback" in interface.lower():
        scapy_if = interface
        break
