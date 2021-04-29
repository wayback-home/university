import os


class Menu(object):
    """dscription of class"""

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.exitNumber = -1
        self.MenuNumber = 0

    def print(self):
        os.system("clear")
        print("\n" * 5)
        print("\t\t\t" + self.title)
        print("\n\n")

        i = 0
        for content in self.contents:
            i += 1
            print("\t\t", end="")
            print(i, end=". ")
            print(content)
            print()

        i += 1
        print("\t\t", end="")
        print(i, end=". ")
        self.exitNumber
        print("종     료")
        print("\n" * 2)
        print("원하는 번호를 입력하세요 : ", end="")

    def getMenuNumber(self):
        menuNumber = input()
        validMenuNumberList = list(str(i) for i in range(1, len(self.contents) + 2))
        while menuNumber not in validMenuNumberList:
            print("\t\t잘못 입력했어요. 다시 입력해주세요")
            print()
            print("\t\t원하는 번호를 다시 입력하세요 : ", end="")
            menuNumber = input()
        self.menuNumber = int(menuNumber)
        # return int(menuNumber)

    def isExit():
        if self.menuNumber == self.exitNumber:
            return True
        else:
            return False

    def getContent(self):
        return self.contents[self.menuNumber - 1]
