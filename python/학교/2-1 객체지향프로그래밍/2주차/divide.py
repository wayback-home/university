import sys

operand1 = sys.argv[1]
operand2 = sys.argv[2]
if operand2 == "0":
    print("0으로 나눌 수 없습니다.")
else:
    print("{0} / {1} = {2}".format(operand1, operand2, int(operand1) / int(operand2)))
