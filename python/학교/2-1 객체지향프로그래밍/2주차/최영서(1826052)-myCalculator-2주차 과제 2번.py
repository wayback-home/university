# 객체지향 프로그래밍 2주차 예제 : 계산기 프로그램 작성 작성, 컴퓨터공학과 2학년 1826052 최영서
import sys

if sys.argv[1] == "/?":
    print("이 프로그램은 사칙연산과 나머지, 몫, 승을 구할 수 있습니다.")
    print("1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료")

else:
    getfunction = input("1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :")
    while getfunction not in "12345678":
        print("잘못 입력하셨습니다. 1에서 8까지의 숫자를 입력하세요.")
        getfunction = input(
            "1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :"
        )

    while getfunction != "8":
        operand1 = input("첫번째 숫자를 입력하세요 : ")
        while not operand1.isdigit():
            print("정수가 아닙니다.")
            operand1 = input("첫번째 숫자를 입력하세요: ")

        intoperand1 = int(operand1)

        operand2 = input("두번째 숫자를 입력하세요 : ")
        while not operand2.isdigit():
            print("정수가 아닙니다.")
            operand2 = input("두번째 숫자를 입력하세요: ")

        intoperand2 = int(operand2)

        if getfunction == "1":
            print(
                "정수열 더하기 : {0} + {1} = {2}".format(
                    operand1, operand2, (intoperand1 + intoperand2)
                )
            )

        if getfunction == "2":
            print(
                "정수열 빼기 : {0} - {1} = {2}".format(
                    operand1, operand2, (intoperand1 - intoperand2)
                )
            )

        if getfunction == "3":
            print(
                "정수열 곱하기 : {0} * {1} = {2}".format(
                    operand1, operand2, (intoperand1 * intoperand2)
                )
            )

        if getfunction == "4":
            print(
                "정수열 나누기 : {0} / {1} = {2}".format(
                    operand1, operand2, (intoperand1 / intoperand2)
                )
            )

        if getfunction == "5":
            print(
                "정수열 나머지 : {0} % {1} = {2}".format(
                    operand1, operand2, (intoperand1 % intoperand2)
                )
            )

        if getfunction == "6":
            print(
                "정수열 몫 : {0} // {1} = {2}".format(
                    operand1, operand2, (intoperand1 // intoperand2)
                )
            )

        if getfunction == "7":
            print(
                "정수열 승 : {0} ** {1} = {2}".format(
                    operand1, operand2, (intoperand1 ** intoperand2)
                )
            )

        print("\n\n\n")

        getfunction = input(
            "1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :"
        )

        while getfunction not in "12345678":
            print("잘못 입력하셨습니다. 다시 입력하세요")
            getfunction = input(
                "1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :"
            )

    print("안녕히가세요.")