menunumber = input("1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :")
while menunumber not in "12345678":
    print("잘못 입력하셨습니다. 다시 입력하세요")
    menunumber = input("1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :")


while menunumber != "8":
    operand1 = input("첫번째 숫자를 입력하세요 : ")
    while not operand1.isdigit():
        print("정수가 아닙니다.")
        operand1 = input("첫번째 숫자를 입력하세요 : ")

    intoperand1 = int(operand1)

    operand2 = input("두번째 숫자를 입력하세요 : ")
    while not operand2.isnumeric():
        print("정수가 아닙니다.")
        operand2 = input("두번째 숫자를 입력하세요 : ")

    intoperand2 = int(operand2)

    print("\n\n")
    print("문자열 더하기 : {0} + {1} = {2}".format(operand1, operand2, operand1 + operand2))
    print("\n")

    if menunumber == "1":
        print(
            "정수열 더하기 : {0} + {1} = {2}".format(
                operand1, operand2, (intoperand1 + intoperand2)
            )
        )

    if menunumber == "2":
        print(
            "정수열 빼기 : {0} - {1} = {2}".format(
                operand1, operand2, (intoperand1 - intoperand2)
            )
        )

    if menunumber == "3":
        print(
            "정수열 곱하기 : {0} * {1} = {2}".format(
                operand1, operand2, (intoperand1 * intoperand2)
            )
        )

    if menunumber == "4":
        print(
            "정수열 나누기 : {0} / {1} = {2}".format(
                operand1, operand2, (intoperand1 / intoperand2)
            )
        )

    if menunumber == "5":
        print(
            "정수열 나머지 : {0} % {1} = {2}".format(
                operand1, operand2, (intoperand1 % intoperand2)
            )
        )

    if menunumber == "6":
        print(
            "정수열 몫 : {0} // {1} = {2}".format(
                operand1, operand2, (intoperand1 // intoperand2)
            )
        )

    if menunumber == "7":
        print(
            "정수열 승 : {0} ** {1} = {2}".format(
                operand1, operand2, (intoperand1 ** intoperand2)
            )
        )

    print("\n\n\n")

    menunumber = input("1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :")

    while menunumber not in "12345678":
        print("잘못 입력하셨습니다. 다시 입력하세요")
        menunumber = input("1. 더하기  2. 빼기  3.곱하기  4. 나누기  5. 나머지  6. 몫  7. 승  8. 종료  :")


print("안녕히가세요.")
