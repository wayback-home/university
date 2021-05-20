from Number import *

op1 = Number("첫번째 숫자를 입력하세요")
op2 = Number("두번째 숫자를 입력하세요")

messageHead = Number.OperatorMessage[0]
print(f"\t{messageHead} : {op1} + {op2} = {op1 + op2}")


messageHead = Number.OperatorMessage[3]
operator = Number.Operator[3]
expression = f"{op1} {operator} {op2}"
result = eval(expression)
print(f"\t{messageHead} : {op1} {operator} {op2} = {result}")
