# 객체지향 프로그래밍 12주차 과제 : 계산기 프로그램 , 컴퓨터공학과 2학년 1826052 최영서
import os


from Number import *
from Menu import *

contents = Number.OperatorMessage
printmenu = Menu(contents)


while not printmenu.isExit():
    printmenu.print()
    printmenu.getMenuNumber()

    print("\n\n")
    op1 = Number("\t첫번째 숫자를 입력하세요")
    op2 = Number("\t두번째 숫자를 입력하세요")

    messageHead = Number.OperatorMessage[printmenu.MenuNumber - 1]
    operator = Number.Operator[printmenu.MenuNumber - 1]
    expression = f"{op1} {operator} {op2}"
    result = eval(expression)
    print(f"\t{messageHead} : {op1} {operator} {op2} = {result}")
    input("\t\t계속하려면 엔터를 누르세요")