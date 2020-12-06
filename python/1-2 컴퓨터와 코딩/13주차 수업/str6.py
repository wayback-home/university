str = input("문자열 입력 :")

n = len(str)

for i in range(n):
    str = str[-1] + str[:-1]
    print(str)

for i in range(n):
    str = str[n - 1] + str[: n - 1]
    print(str)
