data = ['good', 'morning', 'hello', 'welcome']
print(data[1:4:1])
print(data, data[::])
print(data[1:4], data[1:4][0])
print(data[:4])
print(data[1:])
print(data[::2])
print(data[::-2])
data[1:3] = ['bye']
print(data)

az = b'AtoZ'
heart = bytes(b'\xe2\x99\xa5')
print(az)
print(heart)
print(heart.decode())
print(az[1])
print(heart[1], hex(heart[1]))
