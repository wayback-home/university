import os


def Plus(op1, op2):
    return op1 + op2


def Minus(op1, op2):
    return op1 - op2


def Multiply(op1, op2):
    return op1 * op2


def Divide(op1, op2):
    return op1 / op2


def printMenu(title, name, contents):
    os.system("cls")
    print("\n\n\n")
    print("\t\t" + title)
    print("\n\n")

    print("\t\t\t\t" + name)
    print("\n\n")

    i = 0
    for content in contents:
        print("\t", end="")
        i += 1
        print(i, end=". ")
        print(content)
        print()
    print("\t", end="")
    i += 1
    print(i, end=". ")
    print("종  료")
    print("\n\n")
    print("원하는 번호를 선택하세요 : ", end="")


def getMenuNumber():
    menuNumber = input()
    while menuNumber not in ["1", "2", "3", "4", "5"]:
        print("\t틀렸습니다")
        menuNumber = input()
    return menuNumber


def printResult(op1, op2, operater, result):
    print(f"{op1} operater {op2} = {result}")


if "__name__" == "__main__":
    menuTitle = "내가 만든 계산기 프로그램"
    menuContents = ["더하기", "빼기", "곱하기", "나누기"]
    operater = ["+", "-", "X", "/"]
    mycal = [Plus, Minus, Multiply, Divide]

    printMenu(menuTitle, menuContents)
    menuNumber = getMenuNumber()

    while menuNumber != [str(i) for i in range(1, len(menuContents) + 2)]:
        op1 = int(input("첫번째 피연산자를 입력하세요 : "))
        op2 = int(input("두번째 피연산자를 입력하세요 : "))
        print("\t" + menuContents[int(menuNumber) - 1])

        #     print(
        #         f"{op1} {operater[int(menuNumber) - 1]} {op2} = {mycal[int(menuNumber) - 1](op1, op2)}"
        #     )

        printResult(op1, op2, operater[int(menuNumber) - 1], mycal[int(menuNumber) - 1])
        print(menuTitle, menuContents)
        menuNumber = getMenuNumber()

    print("계산기 프로그램 끝")

    print("가위바위보 프로그램 시작")

    menuTitle = "가위바위보 프로그램"
    menuContents = ["가위", "바위", "보"]

    printMenu(menuTitle, menuContents)
    menuNumber = getMenuNumber()

    while menuNumber != str(len(menuContents) + 1):
        print("\t" + menuContents[int(menuNumber) - 1])
        print(menuTitle, menuContents)
        menuNumber = getMenuNumber()

    print("가위바위보 프로그램 종료")