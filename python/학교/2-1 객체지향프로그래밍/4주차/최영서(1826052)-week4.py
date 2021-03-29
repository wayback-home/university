# 객체지향 프로그래밍 4주차 예제, 컴퓨터공학과 2학년 1826052 최영서

#
8 == 100
8 != 100
8 > 100
8 >= 100
8 < 100
8 <= 100

#
love = 80
hate = 70
if love > hate:
    print("당신을 ")
    print("사랑하는 마음이 ")
    print("미워하는 마음보다 큽니다.")

#
if love > hate:
    print("당신을 ")
    print("사랑하는 마음이 ")
    print("미워하는 마음보다 큽니다.")
else:
    print("당신을 ")
    print("원망하는 마음이 ")
    print("사랑하는 마음보다 큽니다.")

#
isLove = True
isHate = False
if isLove and isHate:
    print("당신을 사랑하기도 하고 ")
    print("미워하기도 합니다.")
else:
    print("당신을 사랑하지만 미워하지 않거나 ")
    print("사랑하지 않지만 미워하거나 ")
    print("사랑하지도 미워하지도 않습니다.")

#
isLove = True
isHate = False
if isLove or isHate:
    print("당신을 사랑하거나 ")
    print("미워하거나 그것도 아니면 ")
    print("사랑하지만 미워합니다.")
else:
    print("당신을 사랑하지도 ")
    print("미워하지도 않습니다.")

#
not True
not False

isLove = True
if not isLove:
    print("당신을 사랑하지 않습니다.")
else:
    print("당신을 사랑합니다.")

#
c = 95
python = 95
if c >= 90:
    if python >= 90:
        print("C와 Python, 둘 다 A 입니다")
else:
    print("C가 A가 아닌 것은 알겠는데, Python은 잘 모르겠네요.")

#
c = 95
python = 95
if c >= 90:
    if python >= 90:
        print("C와 Python, 둘 다 A 입니다")
    else:
        pass
else:
    print("C가 A가 아닌 것은 알겠는데, Python은 잘 모르겠네요.")

#
love = 80
hate = 90
if love < hate:
    pass
else:
    print("당신을 사랑합니다.")

#
score = 0
if score >= 60:
    grade = "Pass"
else:
    grade = "Failure"

#
score = int(input("점수를 입력하세요 : "))
if score >= 90:
    print("A학점")
else:
    if score >= 80:
        print("B학점")
    else:
        if score >= 70:
            print("C학점")
        else:
            if score >= 60:
                print("D학점")
            else:
                print("F학점")

#
score = int(input("점수를 입력하세요 : "))
if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")

#
print("type(100) is int : ", type(100) is int)
print("type(100) is not int : ", type(100) is not int)
print("type(지갑) is str : ", type("지갑") is str)
print("type(지갑) is not str : ", type("지갑") is not str)

#
number = input("정수를 입력하세요 : ")
lastCharacter = number[-1]
if (
    lastCharacter == "0"
    or lastCharacter == "2"
    or lastCharacter == "4"
    or lastCharacter == "6"
    or lastCharacter == "8"
):
    print(f"입력한 숫자 {lastCharacter}은 짝수입니다.")
else:
    if (
        lastCharacter == "1"
        or lastCharacter == "3"
        or lastCharacter == "5"
        or lastCharacter == "7"
        or lastCharacter == "9"
    ):
        print(f"입력한 숫자 {lastCharacter}은 홀수입니다.")

#
strNumber = input("정수를 입력하세요 : ")
intNumber = int(strNumber)
if intNumber % 2 == 0:
    print("입력한 숫자 {}은 짝수입니다.".format(intNumber))
else:
    print("입력한 숫자 {}은 홀수입니다.".format(intNumber))

#
import datetime

now = datetime.datetime.now()
intHour = now.hour
if intHour < 5:
    print("게임 그만합시다.")
elif intHour < 8:
    print("학교갑시다.")
elif intHour < 12:
    print("좋은아침~")
elif intHour < 17:
    print("행복한 오후~~~")
elif intHour < 20:
    print("집에 갑시다.")
elif intHour < 23:
    print("이제 잡시다.")
else:
    print("그만 잡시다.")

#
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(f"1부터 100까지의 합은 {sum}입니다.")

#
sum = 0
i = 1
while i <= 100:
    if i % 3 == 0:
        sum += i
    i += 1
print(f"1부터 100까지 3의 배수의 합은 {sum}입니다.")

#
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        if i % 7 != 0:
            sum += i
    i += 1
print(f"1부터 100까지 3의 배수이면서 7의 배수가 아닌 수의 합은 {sum}입니다.")

#
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0:
        if i % 7 != 0:
            sum += i
            break
    else:
        sum += i
print(f"1부터 100까지 3의 배수이면서 7의 배수인 수까지의 합은 {sum}입니다.")

#
count = 1
while count <= 3:
    print(f"{count}. 저를 도와 천하를 도모해 주시겠어요?")
    count += 1
else:
    print(f"{count}. 저를 귀찮게 하는 것이 한두번이 아니네요~ {count-1}번씩이나..")

#
userInput = input("1. 가위  2. 바위  3. 보  4. 종료 : ")
while userInput != "4":
    if userInput == "1":
        print("가위를 냈습니다.")
    elif userInput == "2":
        print("바위를 냈습니다.")
    elif userInput == "3":
        print("보를 냈습니다.")
    else:
        print("잘못 냈네요~")
    userInput = input("1. 가위  2. 바위  3. 보  4. 종료 : ")
print("게임이 끝났습니다. 안녕히가세요!")

#
userInput = input("1. 더하기  2. 빼기  3. 곱하기  4. 나누기  5. 종료 : ")
while userInput != "5":
    op1 = float(input("\t\t첫번째 연산자를 입력하세요 : "))
    op2 = float(input("\t\t두번째 연산자를 입력하세요 : "))
    if userInput == "1":
        print(f"{op1} + {op2} = {op1 + op2}")
    elif userInput == "2":
        print(f"{op1} - {op2} = {op1 - op2}")
    elif userInput == "3":
        print(f"{op1} * {op2} = {op1 * op2}")
    elif userInput == "4":
        print(f"{op1} / {op2} = {op1 / op2}")
    else:
        print("잘못 냈네요")
    userInput = input("1. 더하기  2. 빼기  3. 곱하기  4. 나누기  5. 종료 : ")

print("안녕히 가세요")

#
userInput = input("1. 가위  2. 바위  3. 보  4. 종료 : ")
while True:
    if userInput == "1":
        print("가위를 냈습니다.")
    elif userInput == "2":
        print("바위를 냈습니다.")
    elif userInput == "3":
        print("보를 냈습니다.")
    elif userInput == "4":
        break
    else:
        print("잘못 냈네요~")
    userInput = input("1. 가위  2. 바위  3. 보  4. 종료 : ")
print("게임이 끝났습니다. 안녕히가세요!")

#
i = 1
sum = 0
while i < 100:
    i += 1
    if i % 3 == 0:
        continue
    sum += i
print(f"1부터 100까지의 3의 배수를 제외한 수를 더한 합은 {sum}입니다.")

#
import random


userWincount = 0
comWincount = 0


userName = input("이름을 입력하세요 : ")
print()
print("가위바위보를 합시다~~~~ 가위바위보를 내세요")
userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")
while userResult not in ["1", "2", "3", "4"]:
    print("잘못 냈어요~ 정신좀 차리세요~~")
    userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")

while userResult != "4":
    computerResult = random.randrange(3) + 1

    if computerResult == 1:
        if userResult == "1":
            print((f"{userName} : 가위   컴퓨터 : 가위"))
            print(f"{userName}님과 컴퓨터가 비겼습니다.")
            print("사이좋게 비겼네요~~")

        elif userResult == "2":
            print((f"{userName} : 바위   컴퓨터 : 가위"))
            print(f"{userName}님이 컴퓨터를 이겼습니다.")
            print("감히 나를 이기다니...")
            userWincount += 1

        elif userResult == "3":
            print((f"{userName} : 보   컴퓨터 : 가위"))
            print(f"{userName}님이 컴퓨터에게 졌습니다.")
            print("내가 이겼지롱~~~")
            comWincount += 1

    elif computerResult == 2:
        if userResult == "1":
            print((f"{userName} : 가위   컴퓨터 : 바위"))
            print(f"{userName}님이 컴퓨터에게 졌습니다.")
            print("내가 이겼지롱~~~")
            comWincount += 1

        elif userResult == "2":
            print((f"{userName} : 바위   컴퓨터 : 바위"))
            print(f"{userName}님과 컴퓨터가 비겼습니다.")
            print("사이좋게 비겼네요~~")

        elif userResult == "3":
            print((f"{userName} : 보   컴퓨터 : 바위"))
            print(f"{userName}님이 컴퓨터를 이겼습니다.")
            print("감히 나를 이기다니...")
            userWincount += 1

    elif computerResult == 3:
        if userResult == "1":
            print((f"{userName} : 가위   컴퓨터 : 보"))
            print(f"{userName}님이 컴퓨터를 이겼습니다.")
            print("감히 나를 이기다니...")
            userWincount += 1

        elif userResult == "2":
            print((f"{userName} : 바위   컴퓨터 : 보"))
            print(f"{userName}님이 컴퓨터에게 졌습니다.")
            print("내가 이겼지롱~~~")
            comWincount += 1

        elif userResult == "3":
            print((f"{userName} : 보   컴퓨터 : 보"))
            print(f"{userName}님과 컴퓨터가 비겼습니다.")
            print("사이좋게 비겼네요~~")

    print()
    print("가위바위보를 합시다~~~~ 가위바위보를 내세요")
    userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")
    while userResult not in ["1", "2", "3", "4"]:
        print("잘못 냈어요~ 정신좀 차리세요~~")
        userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")

if userWincount > comWincount:
    print("조만간 또 오세요~ 내가 가위바위보를 더 연습해 놓겠습니다")
elif userWincount < comWincount:
    print("실력 좀 더 쌓은 후에 오세요~~~~~ 아직 내겐 멀었네요~")
else:
    print("안녕히 가세요.")
