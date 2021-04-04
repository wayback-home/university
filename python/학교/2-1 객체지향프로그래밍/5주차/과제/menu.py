# 객체지향 프로그래밍 5주차 예제, 컴퓨터공학과 2학년 1826052 최영서
import time


def printMenu():
    print(
        """
    \t\t\t1. 더하기  2. 빼기  3. 곱하기  4. 나누기  5. 몫 구하기
    \t\t\t6. 나머지 구하기  7. 제곱 구하기  8. 종료
        """
    )
    print("\n")


def getMenuNumber():
    menuNumber = input("\t\t원하는 번호를 선택하세요 : ")
    while menuNumber not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("\t\t잘못 입력하셨습니다. 다시 입력해주세요")
        print("\n\n")
        menuNumber = input("\t\t원하는 번호를 선택하세요 : ")
    return menuNumber
