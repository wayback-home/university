data1 = {'kor': 95, 'eng': 90, 'name': 'hong'}
data2 = dict([('kor', 95), ('eng', 90), ('name', 'hong')])
data3 = dict(kor=95, eng=90, name='hong')
print(data1)
print(data1['kor'])
data1['kor'] = 100
print(data1)
