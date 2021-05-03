# 객체지향 프로그래밍 9주차 과제 : 시 출력 프로그램 , 컴퓨터공학과 2학년 1826052 최영서
from poetry import *
from menu import *
import poet1, poet2, poet3, poet4


title = "시 감상 프로그램"
menuContents = ["진달래 꽃", "초혼", "그리움", "먼 곳에서 부터"]


myMenu = Menu(title, menuContents)
myMenu.print()
menuNumber = myMenu.getMenuNumber()

# 시를 외부 파일에서 불러들어와 출력하게 만들었기 때문에
# poet1~4까지의 파일이 꼭 같은 폴더에 있어야 출력됨(import시 경로지정 안되어 있음)
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