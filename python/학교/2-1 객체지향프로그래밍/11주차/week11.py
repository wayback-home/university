from CatNDog import *


myPets = list()

myMammal = Mammal("무명", "무색")
myMammal.Nurse()
print(myMammal)
myPets.append(myMammal)

print()

myCat = Cat("톰", "검은")
myCat.Nurse()
print(myCat)
myCat.Meow()
myPets.append(myCat)

print()

myDog = Dog("바둑이", "하양")
myDog.Nurse()
print(myDog)
myDog.Bark()
myPets.append(myDog)

myTiger = Tiger("호돌이", "노랑")
myTiger.Nurse()
print(myTiger)
myTiger.Cry()
myPets.append(myTiger)

myLion = Lion("라이언킹", "노랑")
myLion.Nurse()
print(myLion)
myLion.Cry()
myPets.append(myLion)

myLiger = Liger("라이거", "얼룩")
myLiger.Nurse()
print(myLiger)
myLiger.Cry()
myPets.append(myLiger)

print("\n" * 3)
for myPet in myPets:
    print(myPet)
    myPet.Nurse()
    if type(myPet) is Cat:
        myPet.Meow()
    elif type(myPet) is Dog:
        myPet.Bark()
    else:
        print("난 울 수 없어요~")
    print()

    myPet.Cry()
    print()