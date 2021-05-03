import os


class Menu(object):
    """discription of class"""

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

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
        print("종     료")
        print("\n" * 2)

    def getMenuNumber(self):
        menuNumber = input("\t\t원하는 번호를 입력하세요 : ")
        while menuNumber not in ["1", "2", "3", "4", "5"]:
            print("\t\t잘못 입력했어요. 다시 입력해주세요")
            print()
            menuNumber = input("\t\t원하는 번호를 입력하세요 : ")
        self.menuNumber = int(menuNumber)
        return int(menuNumber)