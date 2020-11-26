def func1():
    a = 10
    print("func1에서의 a값 : %d" % a)


def func2():
    print("func2에서의 a값 : %d" % a)


a = 30


func1()  # 지역변수 우선사용
func2()  # 전역변수 사용
