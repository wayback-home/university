from Menu import *

title = "시를 감상합시다"
menuContents = ["진달래 꽃", "초혼", "그리움", "먼 곳에서 부터"]

myMenu = Menu(title, menuContents)
myMenu.print()
# menuNumber = myMenu.getMenuNumber()
myMenu.getMenuNumber()

# while menuNumber != 5:
# while menuNumber != myMenu.exitNumber:
while not myMenu.isExit():
    print()
    # print("\t\t\t" + menuContents[menuNumber - 2])
    print("\t\t\t" + myMenu.getContent())
    myMenu.print()
    menuNumber = myMenu.getMenuNumber()
