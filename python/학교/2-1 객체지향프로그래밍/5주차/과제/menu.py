# 객체지향 프로그래밍 5주차 예제, 컴퓨터공학과 2학년 1826052 최영서
import time


def printMenu():
    print(
        """
    \t\t\t1. 더하기
    \t\t\t2. 빼기
    \t\t\t3. 곱하기
    \t\t\t4. 나누기
    \t\t\t5. 몫 구하기
    \t\t\t6. 나머지 구하기
    \t\t\t7. 제곱 구하기
    \t\t\t8. 종료
        """
    )
    print("\n")
    print("\t\t사용할 기능을 선택해주세요.")
    print("\n")


def getMenuNumber():
    while 1:
        getmenu = int(input())
        if getmenu not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print("\t\t잘못 입력하셨습니다. 1에서 8 사이의 숫자를 입력해주세요")
            printMenu()

        else:
            print("\n\n")
            print("\t\t선택한 기능을 실행합니다", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".", end="")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\n" * 30)
            return getmenu
            break