# 객체지향 프로그래밍 11주차 예제, 컴퓨터공학과 2학년 1826052 최영서


from os import initgroups
from typing import Iterator


class Cat:
    def __init__(self, name, color):
        self._name = name
        self.color = color

    def __str__(self):
        return f"여기는 __str__()입니다. 나는 클래스 Cat의 객체 {self.color}고양이 {self._name} 입니다. "


tom = Cat("톰", "하양")
print(str(tom))
print(tom)


class Dog:
    def __init__(self, name, color):
        self._name = name
        self.color = color

    def __str__(self):
        return f"여기는 __str__()입니다. 나는 클래스 Dog의 객체 {self.color} 강아지 {self._name} 입니다. "


baDugi = Dog("바둑이", "하양")
print(repr(baDugi))
print(baDugi)


class strNrepr(object):
    def __str__(self):
        return f"여기는 __str__()메서드입니다. "

    def __repr__(self):
        return f"여기는 __repr__()메서드입니다. "


a = strNrepr()
b = strNrepr()
print(str(a))
print(repr(a))
print(a)


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def Name(self):
        return self._name

    def WhoAreYou(self):
        print(f"여기는 class Person의 WhoAreYou 메서드입니다. 내 이름은 {self.Name}입니다. 반갑습니다. ")

    def __repr__(self):
        repr1 = (
            f"나는 클래스 Person의 객체 {self.Name}입니다."
            + "\n나를 좋아하지도 미워하지도 마세요."
            + "\n이 몸은 번뇌의 근원이나니"
            + "\n나를 미워해 보았자.."
        )
        return repr1


gilDong = Person("홍길동")
print(gilDong)


class Mammal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Dog(Mammal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def __str__(self):
        return "종류 : 강아지, 이름 : {0}, 색깔 : {1}".format(self.name, self.color)

    def Bark(self):
        print("{0}는 멍멍 짖습니다.").format(self.name)


class Cat(Mammal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def __str__(self):
        return "종류 : 고양이, 이름 : {0}, 색깔 : {1}".format(self.name, self.color)

    def Meow(self):
        print("{0}는 야옹 하고 웁니다.").format(self.name)


tom = Cat("톰", "하양")
print(tom)
baDugi = Dog("바둑이", "하양")
print(baDugi)


class Poetry:
    def __init__(self, title, poet, contents):
        self._title = title
        self._poet = poet
        self._contents = contents

    def __repr__(self):
        repr1 = (
            f"이 시는 {self._poet}님의 {self._title}이란 시입니다."
            + f"\n{len(self._contents)}줄로 이루어진 시이고, 첫 소절은 이렇게 시작합니다."
            + f"\n{self._contents[0]}..."
        )
        return repr1


title = "그리움"
poet = "유치환"
contents = ["파도야 어쩌란 말이냐", "파도야 어쩌란 말이냐", "임은 물같이 까딱 않는데", "파도야 어쩌란 말이냐", "날 어쩌란 말이냐"]
myPoetry = Poetry(title, poet, contents)
print()
print(myPoetry)


class Double(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, number):
        return self.value * 2 + 2 * number

    def __sub__(self, number):
        return self.value * 2 - 2 * number

    def __mul__(self, number):
        return self.value * 2 * 2 * number

    def __truediv__(self, number):
        return self.value * 2 / (2 * number)


d = Double(10)
print(f"10+3 = {d+3}")
print(f"10-4 = {d-4}")
print(f"10*5 = {d*5}")
print(f"10/6 = {d/6}")


class Test:
    def __repr__(self):
        return str(id(self))


class NewInt(Test, int):
    pass


int1 = NewInt(5)
print(int1)
print(int1 + 5)
print(str(int1))
print(repr(int1))


class Call:
    def __call__(self):
        print("__call__()메서드가 호출되었습니다.")
        print("__call__()메서드는 클래스를 함수처럼 호출할 수 있도록 해 줍니다.")


myCall = Call()
myCall()


class Decorator:
    def __init__(self, func):
        print("decorator 클래스의 객체가 생성되었습니다...")
        self.func = func

    def __call__(self):
        print(f"{self.func.__name__}()함수의 장식이 시작되었습니다.")
        self.func()
        print(f"{self.func.__name__}()함수의 장식이 끝났습니다.")


def myFunction():
    print("여기는 myFunction()함수입니다.")


myCall = Decorator(myFunction)
myCall

# iterator = range(3)__iter__()
# try:
#     print(iterator.__next__())
#     print(iterator.__next__())
#     print(iterator.__next__())
#     print(iterator.__next__())
# except Exception as e:
#     print(e)
#     print("예외가 발생했습니다.",e)


class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration()


for i in MyRange(0, 5):
    print(i)


def generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


iterator = generator()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())