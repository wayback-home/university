ㅊ
def sum(arg1, arg2):
    return arg1 + arg2


i = 5
j = 10
k = sum(i, j)
print(k)


def hello():
    print("안녕하세요!")


def hello(name):
    print(f"안녕하세요!{name}님!")


hello("홍길동")


def swap(x, y):
    temp = x
    x = y
    y = temp
    print(f"x = {x}, y = {y}")


i = 10
j = 5
swap(i, j)
print(f"i = {i}, j = {j}")


def swap(x, y):
    temp = x[0]
    x[0] = y[0]
    y[0] = temp
    print(f"x = {x},y = {y}")


i = [10]
j = [20]
swap(i, j)
print(f"i = {i}, j = {j}")

i = 10
j = 20
print(f"i = {i}, j = {j}")


def swap():
    global i, j
    temp = i
    i = j
    j = temp


swap()
print(f"i = {i},j = {j}")

i = 10
j = 20
i = i + j
j = i - j
i = i - j
print(f"i = {i}, j = {j}")


def sum(From, To):
    sum = 0
    for i in range(From, To + 1):
        sum += i
    return sum


result = sum(1, 100)
print(f"1부터 100까지의 누계는 {result}입니다.")
result = sum(From=10, To=20)
print(f"10부터 20까지의 누계는 {result}입니다.")
result = sum(To=50, From=10)
print(f"10부터 50까지의 누계는 {result}입니다.")


def Plus(i, j):
    print(f"{i} + {j} = {i+j}")


def getOperand1():
    return int(input("첫번째 수를 입력하세요 :"))


def getOperand2():
    return int(input("두번째 수를 입력하세요 :"))


operand1 = getOperand1()
operand2 = getOperand2()
Plus(operand1, operand2)


def getOperand1():
    operand = input("첫 번째 숫자를 입력하세요 : ")
    if "." in operand:
        return float(operand)
    else:
        return int(operand)


def getOperand2():
    operand = input("e두 번째 숫자를 입력하세요 : ")
    if "." in operand:
        return float(operand)
    else:
        return int(operand)


def getOperand(operandNumber):
    if operandNumber == 1:
        operand = input("첫 번째 숫자를 입력하세요 : ")
    else:
        operand = input("두 번째 숫자를 입력하세요 :")
    if "." in operand:
        return float(operand)
    else:
        return int(operand)


def getOperand(message):
    operand = input(message)
    if "." in operand:
        return float(operand)
    else:
        return int(operand)


operater = ["더하기", "빼기", "곱하기", "나누기", "종료"]


def getValidMenuNumber():
    menuMessage = ""
    validNumberList = ""
    i = 0
    for menuitem in operator:
        i += 1
        validNumberstring += str(i)
        menuMessage += str(i) + "." + menuitem + " "
    menuNumber = input(menuMessage + " : ")
    while menuNumber not in validNumberstring:
        print("입력하신 번호가 틀렸습니다. 다시 입력해 주세요.")
        menuNumber = input(menuMessage + " : ")
    return int(menuNumber)


listFunc = [Plus, Minus, Multiply, Divide]
menuNumber = getValidMenuNumber()
while operater[menuNumber - 1] != "종료":
    operand1 = getOperand(1)
    operand2 = getOperand(2)
    result = listFunc[menuNumber - 1](operand1, operand2)
    print(f"{operand1} {operatorSymbol[menuNumber-1]}" + f"{operand2} = {result}")
    print()
    menuNumber = getValidMenuNumber()
print("안녕히 가세요!!")


gmaeResult = ["가위", "바위", "보", "종료"]
menuNumber = input("1. 가위 2. 바위 3. 보 4. 종료 :")
while menuNumber != "4":
    result = gameResult[int(menuNumber) - 1]
    print(f"입력하신 번호가 {menuNumber}이니까 {result}를 냈습니다.")
    menuNumber = input("1. 가위 2. 바위 3. 보 4. 종료 :")

from io import IncrementalNewlineDecoder, RawIOBase
import random

PlayList = ["가위", "바위", "보", "종료"]


def printPlayResult(computerPlayResult, userName, userPlayResult):
    print(f"{userName}님 : {userPlayResult}, 컴퓨터 : {computerPlayResult}")
    if computerPlayResult == "가위":
        if userPlayResult == "가위":
            print("{0}님이 컴퓨터와 비겼습니다.".format(userName))

        elif userPlayResult == "바위":
            print("{0}님이 컴퓨터를 이겼습니다.".format(userName))

        elif userPlayResult == "보":
            print("{0}님이 컴퓨터에게 졌습니다.".format(userName))


def getUserResult():
    print()
    inputNumber = input("가위바위보 - 1. 가위  2. 바위  3. 보  4. 종료 : ")
    while inputNumber not in [str(i) for i in range(1, len(PlayList))]:
        print("잘못 냈습니다. 1, 2, 3, 4 만 낼 수 있어요")
        inputNumber = input("가위바위보 - 1. 가위  2. 바위  3. 보  4. 종료 : ")
    return PlayList[int(inputNumber) - 1]


userName = input("이름을 입력하세요 : ")
computerPlayResult = random.choice(PlayList[:-1])
userPlayResult = getUserResult()
while userPlayResult != "종료":
    printPlayResult(computerPlayResult, userName, userPlayResult)
    computerPlayResult = random.choice(PlayList[:-1])
    userPlayResult = getUserResult()


def recursiveCall(count):
    if count == 0:
        print(f"마지막 호출입니다.")
        return
    print(f"{count}번 더 호출할 것입니다.")
    count -= 1
    recursiveCall(count)
    print(f"{3-count}번째 호출을 마칩니다.")


recursiveCall(3)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def hanoi(height, left, middle, right):
    if height == 0:
        return 0
    hanoi(height - 1, left, right, middle)
    move(left, right)
    hanoi(height - 1, middle, left, right)


def move(source, target):
    print(f"{source}의 탑 한층을 {target}으로 옮깁니다.")


def sum(*args):
    print(f"args = {args}")
    sum = 0
    for i in args:
        sum += i
    return sum


result = sum(10, 20, 30, 40, 50)
print(f"sum(10,20,30,40,50)합계는 {result}입니다.")


def compute(operator, *args):
    if operator == "+":
        sum = 0
        for i in args:
            sum += i
    elif operator == "*":
        sum = 1
        for i in args:
            sum *= i
    return sum


def printDic(**argDicts):
    print(argDicts)

printDic(key = 'value')
printDic(name = '홍길동', 나이 = 22)


def divide(x,y):
    return x//y,x%y
i = 10
j = 7
quotient, remainder = divide(i,j)
print(f"i = {i}, j = {j}, 몫 = {quotient}, 나머지 = {remainder}")


def WhoAreYou(name,age,sex="female"):
    if sex == 'female':
        print(f"나는 미즈 {name}이고요, 나이는 {age-10}살 정도..")
    else sex == 'male':
        print(f'나는 미스터{name}이고요, 나이는 {age}살 입니다.')
    else:
        print(f'내 이름은 {name}이고요, 나이는 {age}살이고, 성별은 {sex}입니다.')

sum = lambda x, y:x+y
i = 10
j = 20
result = sum(i,j)
print(f'i = {i}, j = {j}, i + j = {result}')

swap = lambda x,y:(y,x)
i = 10
j = 20
print(f"i = {i}, j = {j}")
i, j = swap(i,j)
print(f"i = {i}, j = {j}")

import math
print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.log(1))

print(math.floor(3.5))
print(math.floor(-3.5))

print(math.ceil(3.4))
print(math.ceil(-3.4))

import random
for i in range(3):
    print(random.random())
    print(random.uniform(10,20))
    print(random.randrange(10))
    print()

import random
for i in range(3):
    list1 = [1,2,3,4,5]
    print(list1)
    random.shuffle(list1)
    print(list1)
    print(random.sample([1,2,3],k = 2))

import sys
print(f"sys.argv : {sys.argv}")
print(f"sys.getwindowsversion(): {sys.getwindowsversion()}")

import os
import timeit
print(f'os.name: {os.name}')
print(f"os.getcwd() : {os.getcwd()}")
print(f"os.listdir() : {os.listdir()}")

import timeit
import datetime
while True :
now = datetime.datetime.now()
print(f'{now.year}:{now.month}:{now.day}'+f"L{now.hour}:{now.mintue}:{now.second}")
timeit.time.sleep(1)


def hello():
    print("\t안녕하세요!")
    print("\t여기는 hello()함수 안입니다. 함수를 실행하고 있는 중입니다.")
print(f"\t여기는 {__name__}프로그램의 시작 지점입니다.")
print(f"\t모듈 이름(__name__) : {__name__}")    
print(f"\t여기는 {__name__} 프로그램의 종료 지점입니다.")

import module1 as module
print()
print(f"여기는 {__name__} 프로그램입니다.")
print("import한 module의 hello() 함수를 호출합니다.")
print()
module.hello()
print()
print("import한 module의 hello()함수 호출이 끝났습니다.")
print(f"모듈 이름 (__name__) : {__name__}")
print()

def hello():
    print("\t안녕하세요!!")
    print("\t여기는 hello()함수 안입니다. 함수를 실행하는 중입니다.")

if __name__ == "__main__":
    print(f"\t여기는 {__name__}프로그램의 시작 지점입니다.")
    print(f"\t모듈이름 (__name__) : {__name__}")
    print(f"\t여기는 {__name__}프로그램의 종료 지점입니다.")