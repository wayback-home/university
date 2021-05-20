class Number(object):
    Operator = ["+", "-", "*", "/"]
    OperatorMessage = ["더하기", "빼기", "곱하기", "나누기"]

    def __init__(self, message):
        self._value = 0
        self._getNumber(message)

    def _getNumber(self, message):
        number = input("\t" + message + ":")
        if number.isnumeric():
            self._value = int(number)
        else:
            self._value = float(number)
        return

    def __str__(self):
        return str(self._value)

    @property
    def Value(self):
        return self._value

    def __add__(self, other):
        return self._value + other.Value

    def __truediv__(self, other):
        if other.Value == 0:
            return "0으로 나눌 수 없습니다."
        else:
            return self._value / other.Value
