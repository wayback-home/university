import os
import time


class Poetry(object):
    def __init__(self, title, poet, contents):
        self.title = title
        self.poet = poet
        self.contents = contents

    def printCLS(self):
        os.system("clear")

    def printTitle(self):
        print("\t\t", end="")
        print(self.title)
        time.sleep(1)

    def printPoet(self):
        print("\t\t\t\t", end="")
        print(self.poet)
        time.sleep(1)
        print()
        time.sleep(1)

    def printContents(self):
        for content in self.contents:
            print("\t", end="")
            print(content)
            time.sleep(1)

    def printBlankLine(self):
        for i in range(24 - len(self.contents)):
            print()
            time.sleep(1)
        input("감상이 끝났으면 아무 키나 누르세요.")

    def print(self):
        self.printCLS()
        self.printTitle()
        self.printPoet()
        self.printContents()
        self.printBlankLine()