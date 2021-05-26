import os


class Menu(object):
    """description of class"""

    # class Menu:

    def __init__(self, operator):
        self.operator = operator
        self._exitNumber = -1
        self._menuNumber = 0

    @property
    def MenuNumber(self):
        return self._menuNumber

    def print(self):
        os.system("cls")
        print("\n" * 2)
        i = 0
        for content in self.operator:
            print("\t\t", end="")
            i += 1
            print(i, end=". ")
            print(content)
            print()

        print("\t\t", end="")
        i += 1
        self._exitNumber = i
        print(i, end=". ")
        print("종    료")
        print("\n" * 2)
        print("\t\t원하는 번호를 선택하세요 : ", end="")

    def getMenuNumber(self):
        menuNumber = input()
        validMenuNumberList = list(str(i) for i in range(1, len(self.operator) + 2))
        while menuNumber not in validMenuNumberList:
            print()
            print("\t\t 잘 못 입력했어요~ 정신 차리세요~~~")
            print()
            print("\t\t원하는 번호를 다시 선택하세요 : ", end="")
            menuNumber = input()

        self._menuNumber = int(menuNumber)

    def isExit(self):
        if self._menuNumber == self._exitNumber:
            return True
        else:
            return False

    def getContent(self):
        return self.operator[self._menuNumber - 1]
