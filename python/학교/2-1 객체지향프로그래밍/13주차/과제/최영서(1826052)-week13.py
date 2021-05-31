# 객체지향 프로그래밍 13주차 예제, 컴퓨터공학과 2학년 1826052 최영서
from functools import singledispatch
from os import remove


@singledispatch
def reverseMe(arg):
    print("여기는 int, float, str 타입 이외의 데이터를 list로 처리합니다. : ", list(reversed(arg)))


@reverseMe.register(int)
def _int(arg):
    str1 = ""
    list1 = list(str(arg))
    for digit in reversed(list1):
        str1 += digit
    int1 = int(str1)
    print("여기는 int형 데이터를 거꾸로 처리하는 곳입니다. : ", int1)


@reverseMe.register(str)
def _string(arg):
    str1 = ""
    list1 = list(str(arg))
    for digit in reversed(list1):
        str1 += digit
    print("여기는 str형 데이터를 거꾸로 처리하는 곳입니다. : ", str1)


@reverseMe.register(float)
def _float(arg):
    str1 = ""
    list1 = list(str(arg))
    for digit in reversed(list1):
        str1 += digit
    float1 = float(str1)
    print("여기는 float형 데이터를 거꾸로 처리하는 곳입니다. : ", float1)


reverseMe("Python")
reverseMe(123)
reverseMe(12.345)
reverseMe([1, 2, 3, 4, 5])
reverseMe((1, 2, 3, 4, 5))


Hello = type("Hello", (), {})
print(Hello)
hello = Hello()
print(hello)


def replace(self, old, new):
    while old in self:
        self[self.index(old)] = new


NewList = type("NewList", (list,), {"descrition": "리스트를 좀 고쳤어요!!", "replace": replace})
list1 = NewList([10, 20, 30, 40, 50, 30])
list1.replace(30, 25)
print(list1)
print(list1.descrition)


class Cat:
    def __str__(self):
        return "나는 고양이입니다."


def Meow():
    print("나는 야옹~ 하고 웁니다.")


myCat = type("NewCat", (Cat,), {"description": "나는 우는 고양이입니다.", "Meow": Meow})
print(myCat)
print(myCat.description)
myCat.Meow


class Mammal:
    def __init__(self, name):
        self._name = name

    @property
    def Name(self):
        return self._name


class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"나는 고양이 {self.Name}입니다."


def Meow(self):
    print(f"{self.Name}:야옹~ 야옹~ 야옹~")


NewCat = type("NewCat", (Cat,), {"desc": "나는 우는 고양이입니다.", "Meow": Meow})
myCat = NewCat("네로")
print(myCat)
print(myCat.desc)
myCat.Meow


class MakeCalcAdd(type):
    def __new__(metacles, name, bases, namespace):
        namespace["description"] = "더하기 계산 클래스입니다."
        namespace["add"] = lambda self, a, b: a + b
        return type.__new__(metacles, name, bases, namespace)


CalcAdd = MakeCalcAdd("CalcAdd", (), {})
myCalc = CalcAdd()
print(myCalc.description)
print(myCalc.add(100, 200))


# class Singleton(type):
#     __instance = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls.__instance:
#             cls.__instance[cls] = super().__call__(*args, **kwargs)
#         return cls.__instances[cls]


# class Hello(metaclass=Singleton):
#     pass


# hello1 = Hello()
# hello2 = Hello()
# print(f"hello1의 주소 : {id(hello1)}")
# print(f"hello2의 주소 : {id(hello2)}")
# print(hello1 is hello2)


class MyMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("metaclass__new__")
        return super().__new__(cls, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("metaclass__init__")
        return super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print("metaclass__call__")
        return super().__call__(*args, **kwargs)


class MyClass(metaclass=MyMetaClass):
    def __init__(self):
        print("child__init__")

    def __call__(self):
        print("child__call__")


print("------------------")
obj = MyClass()


class MyClass:
    value = 0

    def __init__(self):
        MyClass.value += 1


if __name__ == "__main__":
    a = MyClass()
    print(MyClass.value)
    b = MyClass()
    print(MyClass.value)


class A:
    def method(self):
        print("클래스 A의 인스턴스 메서드 method()를 실행 중입니다.")


class B(A):
    def method(self):
        print("클래스 B의 인스턴스 메서드 method()를 실행 중입니다.")


ainstance = A()
ainstance.method()
B().method()


class Calculator:
    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


if __name__ == "__main__":
    print("{0} + {1} = {2}".format(7, 4, Calculator.plus(7, 4)))
    print("{0} - {1} = {2}".format(7, 4, Calculator.minus(7, 4)))
    print("{0} * {1} = {2}".format(7, 4, Calculator.multiply(7, 4)))
    print("{0} / {1} = {2}".format(7, 4, Calculator.divide(7, 4)))


class Counter:
    staticCounter = 0

    @staticmethod
    def getCounter(number=1):
        Counter.staticCounter += number
        return Counter.staticCounter


print(Counter.getCounter())
print(Counter().getCounter(5))
myCounter = Counter()
print(myCounter.getCounter())