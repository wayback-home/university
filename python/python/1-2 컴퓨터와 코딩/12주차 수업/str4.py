ss = "12345"

n = len(ss)

for i in range(n):
    ss = ss[1:] + ss[0]
    print(ss)