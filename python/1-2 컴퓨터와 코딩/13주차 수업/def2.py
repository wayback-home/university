def cal(v1, v2, op):
    if op == "+":
        return v1 + v2
    elif op == "-":
        return v1 - v2
    elif op == "*":
        return v1 * v2
    elif op == "/":
        if v1 >= v2:
            return v1 / v2
        else:
            return v2 / v1
    else:
        return 0


op = input("하고 싶은 연산 선택 : +, -, *, / : ")

v1, v2 = 0, 0
while True:
    if op == "/":
        if v1 == 0:
            v1, v2 = map(int, input("두 수 입력 :").split())
        elif v2 == 0:
            v1, v2 = map(int, input("두 수 입력 :").split())
        else:
            break
    else:
        break

if op == "/":
    if v1 >= v2:
        print("%d %s %d = %5.2f" % (v1, op, v2, cal(v1, v2, op)))
    else:
        print("%d %s %d = %5.2f" % (v2, op, v1, cal(v1, v2, op)))
else:
    print("%d %s %d = %d" % (v1, op, v2, cal(v1, v2, op)))
