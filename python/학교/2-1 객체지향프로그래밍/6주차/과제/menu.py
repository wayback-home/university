from module1 import printMenu
from module1 import getMenuNumber
import os
import time


def printPoetry(title, name, contents):
    printMenu(title, name, contents)
    getMenuNumber()
    # os.system("cls")
    # print("\t\t", title)
    # print("\t\t\t", name)
    # for i in range(0, len(contents) - 1):
    #     print(contents[i])
    #     time.sleep(1)
    #     i += 1
