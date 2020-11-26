def plus(v1, v2):
    return v1 + v2


sum = plus(10, 20)
print(sum)

######################
def plus2(v1, v2):
    sum2 = v1 + v2
    print(sum2)


plus2(20, 30)

a, b = map(int, input("두 수 입력 : ").split())
plus2(a, b)
