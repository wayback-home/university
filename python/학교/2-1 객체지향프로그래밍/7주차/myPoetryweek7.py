from menu import printMenu, getMenuNumber
import os
from time import sleep


def printPoetry(title, poet, contents):
    sleeptime = 1
    os.system("cls")
    print("\n" * 30)
    print("\t\t" + title)
    sleep(sleeptime)
    print()
    sleep(sleeptime)
    print()
    sleep(sleeptime)
    print("\t\t\t\t" + poet)
    sleep(sleeptime)
    print()
    sleep(sleeptime)
    for content in contents:
        print("\t" + content)
        sleep(sleeptime)
    for i in range(23 - int(len(contents))):
        print()
        sleep(sleeptime)

    input("감상이 끝났으면 아무키나 누르세요. ")


def printJinDalRae():
    title = "진달래 꽃"
    poet = "김소월"
    contents = """나보기가 역겨워 가실 때에는
    말없이 고이 보내드리우리다.
    영변에 약산 진달래 꽃
    아름따다 가실길에 뿌리우리다.
    
    나보기가 역겨워 가실 때에는
    말없이 고이 보내드리우리다.
    영변에 약산 진달래 꽃
    아름따다 가실길에 뿌리우리다.
    
    나보기가 역겨워 가실 때에는
    말없이 고이 보내드리우리다.
    영변에 약산 진달래 꽃
    아름따다 가실길에 뿌리우리다."""

    printPoetry(title, poet, contents.split("\n"))


def printChoHon():
    title = "초   혼"
    poet = "김소월"
    contents = """산산히 부서진 이름이여~
    부르다가 내가죽을 이름이여
    
    산산히 부서진 이름이여~
    부르다가 내가죽을 이름이여
    
    산산히 부서진 이름이여~
    부르다가 내가죽을 이름이여"""

    printPoetry(title, poet, contents.split("\n"))


def printUmMaYa():
    title = "엄마야 누나야"
    poet = "김소월"
    contents = """엄마야 누나야 강변 살자
    들에는 금모래 빛
    
    엄마야 누나야 강변 살자
    들에는 금모래 빛
    
    엄마야 누나야 강변 살자
    들에는 금모래 빛"""

    printPoetry(title, poet, contents.split("\n"))


title = "김소월 시선"
contents = ["진달래 꽃", "초   혼", "엄마야 누나야"]
myFunc = [printJinDalRae, printChoHon, printUmMaYa]
printMenu(title, contents)
MenuNumber = getMenuNumber(contents)
while MenuNumber != str(len(contents) + 1):
    myFunc[int(MenuNumber) - 1]
    printMenu(title, contents)
    MenuNumber = getMenuNumber(contents)