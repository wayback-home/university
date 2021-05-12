# 객체지향 프로그래밍 10주차 예제, 컴퓨터공학과 2학년 1826052 최영서


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def whoAreYou(self):
        print(f"나는 클래스 Cat의 객체 {self.color}고양이" + f"{self.name}입니다.")


tom = Cat("톰", "하양")
print(f"나는 클래스 Cat의 객체 {tom.color} 고양이 {tom.name}입니다.")
tom.whoAreYou()
tom.name = "네로"
tom.color = "검은"
print(f"나는 클래스 Cat의 객체 {tom.color} 고양이 {tom.name}입니다.")
tom.whoAreYou


class Cat:
    def __init__(self, name, color):
        self._name = name
        self.color = color

    def whoAreYou(self):
        print(f"나는 클래스 Cat의 객체 {self.color}고양이" + f"{self._name}입니다.")


tom = Cat("톰", "하양")
tom._name = "네로"
tom.color = "검은"
tom.whoAreYou()
print(f"나는 클래스 Cat의 객체 {tom.color} 고양이 {tom._name}입니다.")


class Cat:
    def __init__(self, name, color):
        self._name = name
        self.color = color

    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value


tome = Cat("톰", "하양")
tom.setName("네로")
tom.color = "검은"
print(f"나는 클래스 Cat의 객체 {tom.color}고양이 {tom.getName()}입니다.")


class Cat:
    def __init__(self, name, color):
        self._name = name
        self.color = color

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value


tome = Cat("톰", "하양")
tom.Name = "네로"
tom.color = "검은"
print(f"나는 클래스 Cat의 객체 {tom.color}고양이 {tom.Name}입니다.")


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    def WhoAreYou(self):
        print(f"여기는 class Person의 WhoAreYou()메서드입니다." + f"내 이름은 {self.Name}입니다. 반갑습니다.")


person1 = Person("홍길동")
print(f"나는 class Person 객체 {person1.Nmae}입니다. 잘부탁해요")
person1.Name = "파이썬"
person1.WhoAreYou()
print(f"나는 class Person 객체 {person1.Name}입니다. 잘 부탁해요")


class Base:
    def BaseMethod(self):
        print("나는 기반클래스의 BaseMethod입니다.")


class Derived(Base):
    pass


myBase = Base()
myBase.BaseMethod()
myDrive = Derived()
myDrive.BaseMethod()


class Base:
    def BaseMethod(self):
        print("나는 기반 클래스의 BaseMethod입니다.")


class Derived(Base):
    def BaseMethod(self):
        super().BaseMethod()


myBase = Base()
myBase.BaseMethod()
myDrive = Derived()
myDrive.BaseMethod()


class Base:
    def _BaseMethod(self):
        print("나는 기반 클래스의 BaseMethod입니다.")

    def BaseMethod(self):
        self._BaseMethod()


class Derived(Base):
    def BaseMethod(self):
        super()._BaseMethod()


myBase = Base()
myBase.BaseMethod()
myDrive = Derived()
myDrive.BaseMethod()


class Base:
    def __init__(self, name):
        self._a = name


class Drived(Base):
    def __init__(self, name):
        super().__init__(name)


class X:
    def __init__(self, a):
        self.a = a


class Y(X):
    def __init__(self, a, b):
        self.b = b
        super().__init__(a)


class Z(Y):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)


myData = X(100)
print("myData = X(100) a = {myData.a} ")
myData = Y(100, 200)
print("myData = Y(100, 200) a = {myData.a}, b = {myData.b} ")
myData = Z(10, 20, 30)
print("myData = Z(10, 20, 30) a = {myData.a}, b = {myData.b} c = {myData.c}")


class X:
    def __init__(self):
        self._i = 10
        self.message = "나는 X입니다."

    def _print(self):
        print(self.message)

    def _play(self):
        print("Play.." + self.message)


class Y(X):
    def __init__(self):
        self._i = 20
        self.message = "나는 Y입니다."

    def _print(self):
        print(self.message)


class Z(Y):
    def __init__(self):
        self._i = 30
        self.message = "나는 Z입니다."

    def _print(self):
        print(self.message)

    def _print(self):
        print("Play.." + self.message)

    def doZ(self):
        print("Z안에서 작업중입니다.")

    def test(self, i):
        x = X()
        x._print()
        x._play()
        print("x.i=" + str(i))
        print("x._i=" + str(x._i))
        y = Y()
        y._print()
        y._play()
        print("y.i=" + str(y._i))

    def test(self, i):
        z = Z()
        y = Z
        x = Z
        z._print
        y._print
        x._print
        z._play
        y._play
        x._play

        super()._print()
        self._play()
        super()._play()
        print("i = " + str(i))
        print("y._i = " + str(y._i))
        print("x._i = " + str(x._i))
        print("z._i = " + str(z._i))
