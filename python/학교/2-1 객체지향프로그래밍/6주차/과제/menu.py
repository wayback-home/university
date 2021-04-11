import os


def printMenu(title, name, contents):
    os.system("cls")
    print("\n\n\n")
    print("\t\t" + title)
    print("\n")

    print("\t\t\t\t" + name)
    print("\n")

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
    print("\t원하는 시의 번호를 선택하세요 : ", end="")


def getMenuNumber():

    menuNumber = input()
    while menuNumber not in ["1", "2", "3", "4", "5"]:
        print("\t틀렸습니다")
        menuNumber = input()
    return menuNumber
