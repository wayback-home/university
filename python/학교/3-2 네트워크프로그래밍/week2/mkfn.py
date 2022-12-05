import struct

negative1 = struct.pack('>i', -1)
f1_5 = struct.pack('>f', 1.5)
fm1_5 = struct.pack('>f', -1.5)
print(negative1)
print(hex(f1_5[0]),hex(f1_5[1]), hex(f1_5[2]), hex(f1_5[3]))
print(fm1_5)
