class String:
    def __init__(self, tmpstr='unnamed'):
        self.data = tmpstr
    def get(self):
        return self.data
    def toBytes(self):
        return self.data.encode()
    def fromBytes(self, bytestr):
        self.data = bytestr.decode()
    def toFile(self, filename):
        fd = open(filename, 'wb')
        fd.write(self.toBytes())
        fd.close()
    def fromFile(self, filename):
        fd = open(filename, 'rb')
        self.fromBytes(fd.read())
        fd.close()

obj = String('홍길동')
obj.toFile('data.bin')
obj.fromBytes('이순신'.encode())
print(obj.get())
obj.fromFile('data.bin')
print(obj.get())