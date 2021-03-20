# 객체지향 프로그래밍 3주차 예제, 컴퓨터공학과 2학년 1826052 최영서


########################
######  3주 1회차 ######
########################


#   문자열이란?
str1 = "당신을 사랑합니다."
str1 = "a"
str1 = "123"
str1 = "Life is too short, You need Python"

print("당신을 사랑합니다")
print("a", "b", "c", "d")
print("Life is too short", ",", "You need Python")


#   문자열의 자료구조
s1 = "Hello"
print(len(s1))


#   문자열 만들기
print("Hello World")
print("파이썬은 쉽다")
print("""Life is too short, You need python""")
print("""인생은 짧으니, 파이썬을 써야해~""")


#   따옴표 안에 따옴표 넣기
###         My favorite Song is "I can't stop me." => Syntax Error
###         >>>>>>>>>>>
###         >>>>>>>>>>>
hisStory = 'My favorite song is "I can\'t stop me."'
print(hisStory)
hisStory = 'My favorite song is "I can\'t stop me."'
print(hisStory)


#   이스케이프 문자(escape character)
myQuotes = "인생은 짧다.\n따라서 프로그래밍은 파이썬으로..."
print(myQuotes)

myQuotes = "인생은 짧다\n따라서" + "프로그래밍은 파이썬으로..."
print(myQuotes)

myQuotes = """인생은 짧다.
따라서 프로그래밍은 파이썬으로..."""
print(myQuotes)

myQuotes = """
인생은 짧다.
따라서 프로그래밍은 파이썬으로...
"""
print(myQuotes)


#   문자열 연결하기 : +, *
me = "I am"
state = " happy!"
myState = me + state
print(myState)  # >>>>>>>>>>>>>     I am happy!

me = "I am"
state = " happy!"
myState = me + state
print((myState + "\n") * 3)

print("\n" * 40)


#   문자열 색인 : indexing
hello = "Hello"
print(hello[0])  # >>>>H
print(hello[1])  # >>>>e

hello = "Hello"
###           print(hello[5])
###           >>>>>> IndexError

hello = "Hello"
print(hello[len(hello) - 1])  # >>>>>> o

hello = "Hello"
print(hello[-1])  # o
print(hello[-0])  # H
print(hello[-len(hello)])  # H


# 문자열 자르기 : slicing
myState = "I am happy!"
state = myState[5] + myState[6] + myState[7] + myState[8] + myState[9]
print(state)  # happy

myState = "I am happy!"
print(myState[5:9])  # happ

myState = "I am happy!"
print(myState[:4])  # I am

myState = "I am happy!"
print(myState[5:])  # happy!

myState = "I am happy!"
print(myState[:])  # I am happy!


# 문자열 꾸미기 : formatting
"%s님 안녕하세요!!" % "홍길동"
name = input("이름을 입력해 주세요 : ")  # 홍길동 입력
print("%s님! 안녕하세요!!!" % name)

age = 20
print("파이썬님의 나이는 %d살 입니다." % age)

name = input("이름을 입력해 주세요 : ")
age = 20
print("%s님의 나이는 %d살 입니다." % (name, age))


########################
######  3주 2회차 ######
########################


# 문자열 꾸미기 : formatting
pi = 3.14159
print("Pi의 값은 %d입니다" % pi)
print("Pi의 값은 %f입니다." % pi)
print("Pi의 값은 %s입니다." % pi)

#       rate = 0.215
#       print("이자율은 %f %입니다."%rate)
#       >>>> TypeError
#       >>>>
rate = 0.215
print("이자율은 %f %%입니다." % rate)

print("%10s 홍길동!" % "안녕하세요~")
print("%-10s 홍길동!" % "안녕하세요~")

pi = 3.14159
print("Pi의 값은 %10.4f입니다" % pi)


# format() 함수로 숫자를 문자열로 변환 1
"{}".format(10)
"{} {}".format(10, 20)
"{} {} {} {} {}".format(101, 202, 303, 404, 505)

# format() 함수로 숫자를 문자열로 변환 2
format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

name = input("이름을 입력해 주세요 : ")
print("{0}님! 안녕하세요!!!".format(name))
age = 20
print("파이썬님의 나이는 {0}살 입니다.".format(age))
print("{0}님의 나이는 {1}살 입니다.".format(name, age))

rate = 0.215
print("이자율은 {0}%입니다.".format(rate))

Hello = "Hello"
print("{0:>10}".format(hello))
print("{0:!>10}".format(hello))
print("{0:<10}".format(hello))
print("{0:!<10}".format(hello))
print("{0:^10}".format(hello))
print("{0:!^10}".format(hello))

pi = 3.14159
print("Pi의 값은 {0:4f}입니다.".format(pi))
print("Pi의 값은 {0:0.4f}입니다.".format(pi))
print("Pi의 값은 {0:10.4f}입니다.".format(pi))

print('1234567890  "{:d}".format(123)\n' + "{:d}".format(123))
print('1234567890  "{:05d}".format(123)\n' + "{:05d}".format(123))
print('1234567890  "{:08d}".format(123)\n' + "{:08d}".format(123))
print('1234567890  "{:08d}".format(-123)\n' + "{:08d}".format(-123))
print('1234567890  "{:+d}".format(123)\n' + "{:05d}".format(123))
print('1234567890  "{:+d}".format(-123)\n' + "{:08d}".format(-123))

print('1234567890  "{:+8d}".format(123)\n' + "{:+8d}".format(123))
print('1234567890  "{:+8d}".format(-123)\n' + "{:+8d}".format(-123))
print('1234567890  "{:=+8d}".format(123)\n' + "{:=+8d}".format(123))
print('1234567890  "{:=+8d}".format(-123)\n' + "{:=+8d}".format(-123))
print('1234567890  "{:+08d}".format(123)\n' + "{:08d}".format(123))
print('1234567890  "{:+08d}".format(-123)\n' + "{:08d}".format(-123))

print('12345678901234567890  "{:f}".format(123.456)\n' + "{:f}".format(123.456))
print('12345678901234567890  "{:f}".format(-123.456)\n' + "{:f}".format(-123.456))
print('12345678901234567890  "{:18f}".format(123.456)\n' + "{:18f}".format(123.456))
print('12345678901234567890  "{:18f}".format(-123.456)\n' + "{:18f}".format(-123.456))
print('12345678901234567890  "{:+18f}".format(123.456)\n' + "{:+18f}".format(123.456))
print('12345678901234567890  "{:+18f}".format(-123.456)\n' + "{:+18f}".format(-123.456))


# 문자열 꾸미기 : formatting
# f-string formatting
rate = 0.215
print(f"이자율은 {rate}%입니다.")

pi = 3.14159
print(f"Pi의 값은 {pi:4f}입니다.")
print(f"Pi의 값은 {pi:0.4f}입니다.")
print(f"Pi의 값은 {pi:10.4f}입니다.")


# 문자열 관련 메서드
# count() 메서드
str = "happy"
print(str.count("p"))

# find() 메서드
str = "I am happy!"
str.find("p")
str.find("b")

# index() 메서드
str = "I am happy!"
print(str.index("p"))
#       print(str.index('p'))
#       >>>>>>> ValueError

# join() 메서드
print("-".join("1234"))
print(",".join(["a", "b", "c", "d"]))

# upper() 메서드
str = "python is too hard."
print(str.upper())

# lower() 메서드
str = "python is too hard."
print(str.lower())

# lstrip() 메서드
str = "    Python    "
print(str.lstrip())

# rstrip() 메서드
str = "    Python    "
print(str.rstrip())

# strip() 메서드
str = "    Python    "
print(str.strip())

myQuotes = """
인생은 짧다.
따라서 프로그래밍은 파이썬으로...
"""
print(myQuotes.strip())

# replace() 메서드
str = "Python is too hard."
print(str.replace("hard", "easy"))

# split() 메서드
str = "Python is too easy."
print(str.split())

str = "a:b:c:d"
print(str.split(":"))

# find(), rfind()
print("고요한 밤 거룩한 밤 어둠에 묻힌 밤".find("밤"))
print("고요한 밤 거룩한 밤 어둠에 묻힌 밤".rfind("밤"))

# +, *, in
print("밥" in "고요한 밤 거룩한 밤 어둠에 묻힌 밤")
print("밤" in "고요한 밤 거룩한 밤 어둠에 묻힌 밤")


########################
######  3주 3회차 ######
########################


# isdigit(), isnumeric(), isdecimal
print(f"{'123'.isdigit()}")
print(f"{{'123'.isdigit()}} : {'123'.isdigit()}")
print(f"{{'123'.isnumeric()}} : {'123'.isnumeric()}")
print(f"{{'123'.isdecimal()}} : {'123'.isdecimal()}")

print()
print(f"{{'①'.isdigit()}} : {'①'.isdigit()}")
print(f"{{'①'.isnumeric()}} : {'①'.isnumeric()}")
print(f"{{'①'.isdecimal()}} : {'①'.isdecimal()}")

print()
print(f"{{'ⅲ'.isdigit()}} : {'ⅲ'.isdigit()}")
print(f"{{'ⅲ'.isnumeric()}} : {'ⅲ'.isnumeric()}")
print(f"{{'ⅲ'.isdecimal()}} : {'ⅲ'.isdecimal()}")

print()
print(f"{{'三'.isdigit()}} : {'三'.isdigit()}")
print(f"{{'三'.isnumeric()}} : {'三'.isnumeric()}")
print(f"{{'三'.isdecimal()}} : {'三'.isdecimal()}")


# sys.argv 오류 예외처리
import sys

if len(sys.argv) == 1 or sys.argv[1] == "/?":
    print(
        """
    이 프로그램의 사용 방법은
    도스 명령창에서 python subtract.py <인수 1> <인수 2>와 같습니다
    <인수 1>이 "/?"일 경우에는 도움말을 출력합니다
    <인수 1>과 <인수 2>가 정수일 경우에는 <인수 1>에서 <인수 2>를 뺀 값을 출력합니다
    """
    )

else:
    print(f"{sys.argv[1]} - {sys.argv[2]} =  {int(sys.argv[1]) - int(sys.argv[2])}")


# 시 출력 프로그램
import time
import os

os.system("cls")
print()
print("\t\t\t시를 감상합시다\n")
print("\t\t1. 시1~~~~~~~~~\n")
print("\t\t2. 시2~~~~~~~~~\n")
print("\t\t3. 시3~~~~~~~~~\n")
print("\t\t4. 종 료")

menunumber = input("감상하려는 시의 번호를 입력하세요 : ")

while menunumber != "4":
    print("\n" * 40)
    if menunumber == "1":
        print("\t1번 시 1번 시 1번 시 1번 시 1번 시")
        time.sleep(1)
        print("\t1번 시 1번 시 1번 시 1번 시 1번 시")
        time.sleep(1)
        print("\t1번 시 1번 시 1번 시 1번 시 1번 시")
        time.sleep(1)
        print("\t1번 시 1번 시 1번 시 1번 시 1번 시")
        time.sleep(1)
        print("\t1번 시 1번 시 1번 시 1번 시 1번 시")
        time.sleep(1)
        print("\t1번 시 1번 시 1번 시 1번 시 1번 시")
        time.sleep(1)
        print("\t1번 시 1번 시 1번 시 1번 시 1번 시")
        time.sleep(1)
        input("감상이 끝났으면 아무키나 누르세요")

    elif menunumber == "2":
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        print("\t2번 시 2번 시 2번 시 2번 시 2번 시")
        time.sleep(1)
        input("감상이 끝났으면 아무키나 누르세요")

    elif menunumber == "3":
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        print("\t3번 시 3번 시 3번 시 3번 시 3번 시")
        time.sleep(1)
        input("감상이 끝났으면 아무키나 누르세요")

    else:
        print("이 프로그램의 사용법은 ....")
        print("이 프로그램의 사용법은 ....")
        print("이 프로그램의 사용법은 ....")
        print("이 프로그램의 사용법은 ....")
        print("이 프로그램의 사용법은 ....")

    print()
    print("\t\t\t시를 감상합시다\n")
    print("\t\t1. 시1~~~~~~~~~\n")
    print("\t\t2. 시2~~~~~~~~~\n")
    print("\t\t3. 시3~~~~~~~~~\n")
    print("\t\t4. 종 료")

    menunumber = input("감상하려는 시의 번호를 입력하세요 : ")

print("안녕히 가세요")