import os
import calculator


def printmenu():
    os.system("cls")
    print("\n\n")
    print("\t\t계산기 프로그램")
    print("\n\n")
    print("\t1. 더    하   기")
    print("\t2. 빼         기")
    print("\t3. 곱    하   기")
    print("\t4. 나    누   기")
    print("\t5. 몫   구 하 기")
    print("\t6. 나머지 구하기")
    print("\t7. 승   구 하 기")
    print("\t8. 종         료")


def getMenuNuber():
    menuNumber = input("원하는 번호를 선택하세요 : ")
    while menuNumber not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("\t잘못 입력하셨습니다. 다시 입력해주세요")
        print("\n\n")
        menuNumber = input("원하는 번호를 선택하세요 : ")
    return menuNumber


def getOperand(message):
    operand = input("\t" + message + " : ")
    while operand.isdigit:
        if "." in operand:
            list1 = operand.split(".")
            if len(list1) > 2:
                print("\t점을 두개 입력했어요")
        elif not list1[0].isdigit():
            print("\t점 앞의 숫자를 잘못 입력했어요")

        elif not list1[1].isdigit():
            print("\t점 뒤의 숫자를 잘못 입력했어요")

        else:
            return float(operand)

        print("\t잘못 입력 했어요. 숫자를 입력하세요.")
        operand = input("\t" + message + " : ")
    return int(operand)


printmenu()
menunumber = getMenuNuber()
while menunumber != "8":
    operand1 = getOperand("첫 번째 피연산자를 입력하세요")
    operand2 = getOperand("두 번째 피연산자를 입력하세요")
    if menunumber == "1":
        calculator.plus(operand1, operand2)
    elif menunumber == "2":
        calculator.minus(operand1, operand2)
    elif menunumber == "3":
        calculator.multi(operand1, operand2)

    printmenu()
    menunumber = getMenuNuber()
