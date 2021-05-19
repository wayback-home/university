# 객체지향 프로그래밍 10주차 과제 : 동물 상속관계 프로그램 , 컴퓨터공학과 2학년 1826052 최영서

from CatNDog import *


myPets = list()

myCat = Cat("톰", "검은")
myPets.append(myCat)


myDog = Dog("바둑이", "하양")
myPets.append(myDog)

myTiger = Tiger("호돌이", "노랑")
myPets.append(myTiger)

myLion = Lion("라이언킹", "노랑")
myPets.append(myLion)

myLiger = Liger("라이거", "얼룩")
myPets.append(myLiger)

print("\n" * 3)
for myPet in myPets:
    print(myPet)
    result = isinstance(myPet, Mammal)
    print(result)

    myPet.Nurse()
    myPet.Cry()

    print("\n\n")