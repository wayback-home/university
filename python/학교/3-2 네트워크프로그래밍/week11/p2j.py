import json

data = dict()
data['name'] = 'hong'
data['age'] = 20
data['flag'] = True
data['goods'] = None
jstr = json.dumps(data)
print(jstr)

fd = open('data.dat','w')
json.dump(data, fd)
fd.close()

rfd = open('data.dat','r')
data2 = json.load(rfd)
print(data2)



d = json.loads(jstr)
print(type(d))
print(d['age'])

e = json.loads('{"w": 22}')
print(type(e))
print(e['w'])

print('=' * 40)

lst = [1, 2, 3, 4, 'kim', 3.14]
jstr2 = json.dumps(lst)
print(jstr2)
print(type(jstr2))

print('=' * 40)
lst2 = json.loads('[ 3.14, 2, "HONG"]')
print(type(lst2))
print(lst2)

