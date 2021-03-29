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

isLove =True
if no isLove:
    print("당신을 사랑하지 않습니다.")
else:
    print("당신을 사랑합니다.")

#
c = 95
python = 95
if c >= 90 :
    if python >= 90:
        print("C와 Python, 둘 다 A 입니다")
else:
    print("C가 A가 아닌 것은 알겠는데, Python은 잘 모르겠네요.")

#
c = 95
python = 95
if c >= 90 :
    if python >=90:
        print("C와 Python, 둘 다 A 입니다")
    else:
        pass
else:
    print("C가 A가 아닌 것은 알겠는데, Python은 잘 모르겠네요.")

#
love =80
hate=90
if love <hate:
    pass
else:
    print("당신을 사랑합니다.")

#
if score>=60:
    grade="Pass"
else:
    grade = "Failure"

#
score = int(input("점수를 입력하세요 : "))
if score>=90 :
    print("A학점")
else:
    if score>=80:
        print("B학점")
    else:
        if score>=70:
            print("C학점")
        else:
            if score>=60:
                print("D학점")
            else:
                print("F학점")

#
score=int(input("점수를 입력하세요 : "))
if score >=90:
    print("A학점")
elif score >=80:
    print("B학점")
elif score >=70:
    print("C학점")
elif score >=60:
    print("D학점")
else:
    print("F학점")