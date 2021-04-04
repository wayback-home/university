# 객체지향 프로그래밍 5주차 계산기 만들기, 컴퓨터공학과 2학년 1826052 최영서
import sys
import calculator
import menu


def getOperand():
    while 1:
        number1 = input("\t\t첫번째 숫자를 입력하세요 : ")
        if number1.isdecimal:
            number1 = int(number1)
            break

        elif number1.isdecimal:
            number1 = float(number1)
            break
        else:
            print("\t\t잘못 입력하셨습니다. 다시 입력해주세요.")

    while 1:
        number2 = input("\t\t첫번째 숫자를 입력하세요 : ")
        if number2.isdecimal:
            number2 = int(number2)
            break

        elif number2.isdecimal:
            number2 = float(number2)
            break
        else:
            print("\t\t잘못 입력하셨습니다. 다시 입력해주세요.")
    return number1, number2


def printResult(op1, op2):
    while menu.getMenuNumber() != 8:
        if menu.getMenuNumber() == 1:
            print(f"\t\t{op1} + {op2} = {calculator.plus(op1, op2)}")

        elif menu.getMenuNumber() == 2:
            print(f"\t\t{op1} - {op2} = {calculator.minus(op1, op2)}")

        elif menu.getMenuNumber() == 3:
            print(f"\t\t{op1} * {op2} = {calculator.multi(op1, op2)}")

        elif menu.getMenuNumber() == 4:
            print(f"\t\t{op1} / {op2} = {calculator.divide(op1, op2)}")

        elif menu.getMenuNumber() == 5:
            print(f"\t\t{op1} // {op2} = {calculator.quotient(op1, op2)}")

        elif menu.getMenuNumber() == 6:
            print(f"\t\t{op1} % {op2} = {calculator.remainder(op1, op2)}")

        elif menu.getMenuNumber() == 7:
            print(f"\t\t{op1} ** {op2} = {calculator.square(op1, op2)}")


if len(sys.argv) == 2 and sys.argv[1] == "/?":
    print("\n" * 30)
    print("\t\t이 프로그램은 계산기입니다.")
    print("\t\t실행 가능한 동작 목록")
    print(
        """
    \t\t\t1. 더하기
    \t\t\t2. 빼기
    \t\t\t3. 곱하기
    \t\t\t4. 나누기
    \t\t\t5. 몫 구하기
    \t\t\t6. 나머지 구하기
    \t\t\t7. 제곱 구하기
    \t\t\t6. 종료
    """
    )
    print("\n\n")

else:
    while menu.getMenuNumber != "8":
        menu.printMenu()

        menunumber = menu.getMenuNumber()

        operand = getOperand()
        printResult(operand[0], operand[1])

    print("\t\t종료합니다.")
    print("\n")