ss = "파이썬재미있다"
count = len(ss)

for i in range(0, count):
    print(ss[i] + "#", end=" ")

outss = ""

for i in range(0, count):
    outss += ss[count - (i + 1)]

print("원래내용 ===> %s" % ss)
print("내용 거꾸로 ===> %s" % outss)


for i in range(0, count):
    if ss[i] != " ":
        outss += ss[i]
print("원래내용 ==> %s" % ss)
print("공백 제거내용 ==>%s" % outss)
