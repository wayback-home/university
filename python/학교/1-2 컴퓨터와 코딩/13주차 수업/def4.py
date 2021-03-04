def func1(*num):  # 튜플로 리스트 지역변수 갯수 상관없이 받기
    result = 0
    for i in num:
        result += i
    return result


sum = func1(10, 20)
print(sum)

sum = func1(10, 20, 20)
print(sum)


def func2(**num):  # 딕셔너리로 받기
    for i in num.keys():
        print(i, "의 값은:", num[i])


func2(A=2, B=3, C=5)
