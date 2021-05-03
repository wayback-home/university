# 객체지향 프로그래밍 9주차 과제 : 시 출력 프로그램 , 컴퓨터공학과 2학년 1826052 최영서
from poetry import *
from menu import *
import poet1, poet2, poet3, poet4


title = "시 감상 프로그램"
menuContents = ["진달래 꽃", "초혼", "그리움", "먼 곳에서 부터"]


myMenu = Menu(title, menuContents)
myMenu.print()
menuNumber = myMenu.getMenuNumber()


while menuNumber != 5:
    if menuNumber == 1:
        Poet = Poetry(poet1.title, poet1.poet, poet1.contents)
        Poet.print()

    elif menuNumber == 2:
        Poet = Poetry(poet2.title, poet2.poet, poet2.contents)
        Poet.print()

    elif menuNumber == 3:
        Poet = Poetry(poet3.title, poet3.poet, poet3.contents)
        Poet.print()

    elif menuNumber == 4:
        Poet = Poetry(poet4.title, poet4.poet, poet4.contents)
        Poet.print()


if menuNumber == 5:
    print("\t\t프로그램을 종료합니다.")