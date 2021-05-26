# 객체지향 프로그래밍 12주차 예제, 컴퓨터공학과 2학년 1826052 최영서
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

    def _play(self):
        print("Play.." + self.message)

    def doZ(self):
        print("Z안에서 작업중입니다.")

    def test(self, i):
        x = X()
        x._print()
        x._play
        print("x.i=" + str(i))
        print("x._i=" + str(x._i))
        y = Y()
        y._print()
        y._play()
        print("y.i=" + str(y._i))


z = Z()
z.test(40)


class Mammal:
    def __init__(self, name):
        self._name = name

    def Nurse(self):
        print("{0}은 수유동물입니다.".format(self._name))


class Dog(Mammal):
    def __init__(self, name):
        self._name = name

    def Bark(self):
        print("{0}은 멍멍 짖습니다.".format(self._name))


class Cat(Mammal):
    def __init__(self, name):
        self._name = name

    def Meow(self):
        print("{0}은 야옹 하고 웁니다.".format(self._name))


myMammal = Mammal("포유동물")
myMammal.Nurse()
myDog = Dog("바둑이")
myDog.Nurse()
myDog.Bark()
print()
myCat = Cat("네로")
myCat.Nurse()
myCat.Meow()
print()
myMammals = [myMammal, myDog, myCat]
for myMammal in myMammals:
    myMammal.Nurse()
    if isinstance(myMammal, Dog):
        myMammal.Bark()
    if isinstance(myMammal, Cat):
        myMammal.Meow()
    print()


class Tiger:
    def __init__(self):
        self._name = "엄마"

    def WhoAreYou(self):
        print("나는 {0}클래스 Tiger 입니다.".format(self._name))


class Lion:
    def __init__(self):
        self._name = "아빠"

    def WhoAreYou(self):
        print("나는 {0}클래스 Lion 입니다.".format(self._name))


class Liger(Tiger, Lion):
    def __init__(self):
        self._name = "아기"

    def WhoAreYou(self):
        print("나는 서브클래스 Liger {0} 입니다.".format(self._name))
        super().WhoAreYou()


myTiger = Tiger()
myTiger.WhoAreYou()
myLion = Lion()
myLion.WhoAreYou()
myLiger = Liger()
myLiger.WhoAreYou()


class Ridable:
    def Ride():
        pass


class Car(Ridable):
    def Run(self):
        print("Run!!!")

    def Ride(self):
        self.Run()


class Plane(Ridable):
    def Fly(self):
        print("Fly")

    def Ride(self):
        self.Fly


class myVehicle(Car, Plane):
    def __init__(self):
        super().Ride()


myRider = myVehicle()
myRider.Ride()


import random


class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")


class C(A):
    def method(self):
        print("C")


A().method()
B().method()
C().method()
list1 = [A(), B(), C()]
random.shuffle(list1)
for obj in list1:
    obj.method()


class PolyA:
    def __init__(self, msg="I am PolyA!"):
        self.msg = msg

    def work(self):
        print("PolyA is working")
        print("PolyA:work:msg = " + self.msg)


class PolyB(PolyA):
    def __init__(self):
        super().__init__("I am PolyB!")

    def work(self):
        print("PolyB is working")
        print("PolyB:work:msg = " + self.msg)


a = PolyA()
a.work()
b = PolyB()
b.work()


class PolyA:
    def __init__(self, msg="I am PolyA!"):
        self._msg = msg

    def init(self):
        self.work()

    def work(self):
        print("PolyA is working")
        print("PolyA:work:msg = " + self._msg)


class PolyB(PolyA):
    def __init__(self):
        super().__init__("I am PolyB!!")

    def work(self):
        print("PolyB is working.")
        print("PolyB:work:msg=" + self._msg)


print()
a = PolyA()
a.init()
print()
b = PolyB()
b.init()