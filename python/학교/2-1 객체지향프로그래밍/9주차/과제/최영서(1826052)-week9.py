# 객체지향 프로그래밍 7, 9주차 예제, 컴퓨터공학과 2학년 1826052 최영서

a = [1, 2, 3]
try:
    print(a[3])
except:
    print("오류가 발생했습니다!")


a = [1, 2, 3]
try:
    print(a[3])
except:
    print("오류가 발생했습니다!")
else:
    print("오류가 발생하지 않았습니다.")


a = [1, 2, 3]
try:
    print(a[3])
except:
    print("오류가 발생했습니다!")
else:
    print("오류가 발생하지 않았습니다.")
finally:
    print("예외처리를 위한 try문이 끝났습니다.")


print("프로그램 시작")
while True:
    try:
        print("try문의 break문 앞")
        break
        print("try문의 break문 뒤")
    except:
        print("except문 시작")
        break
    finally:
        print("finally문 시작")
print("프로그램 종료")


def finallyTest():
    print("finallyTest()함수 시작")
    try:
        print("try문의 return 문 앞")
        return
        print("try문의 return 문 뒤")
    except:
        print("except문 실행")
    finally:
        print("finally문 실행")


print("프로그램 시작")
finallyTest()
print("프로그램 종료")


list1 = [0, 1, 2]
try:
    i = int(input())
    result = list1[i] / i
    print(f"{list1[i]}/{i} = {result}")
except Exception as e:
    print("type(e) :", type(e))
    print("e :", e)


list1 = [0, 1, 2]
try:
    i = int(input())
    result = list1[i] / i
    print(f"{list1[i]}/{i} = {result}")
except ZeroDivisionError:
    print("0 나눔 오류가 발생했습니다.")
except IndexError:
    ("인덱스를 벗어나는 오류가 발생했습니다.")
except Exception:
    print("예기치 못한 오류가 발생했습니다.")


list1 = [0, 1, 2]
try:
    i = int(input())
    result = list1[i] / i
    print(f"{list1[i]}/{i} = {result}")
    j = input()
    if j not in ["0", "1", "2"]:
        result / j
    else:
        raise NotImplementedError

except ZeroDivisionError as e:
    print(f"0 나눔 오류가 발생했습니다. : {e}")
except ValueError as e:
    print(f"정수로 바꿀 수 없습니다. : {e}")
except IndexError as e:
    (f"인덱스를 벗어나는 오류가 발생했습니다. : {e}")
except Exception:
    print(f"예기치 못한 오류가 발생했습니다. : {e}")
finally:
    print("파이썬 오류테스트 끝")


inputData = input("문제 수를 입력하세요")
if inputData.isdigit():
    total = int(inputData)
else:
    print("숫자를 입력하지 않았습니다.")


inputData = input("문제 수를 입력하세요")
while not inputData.isdigit():
    print("숫자를 입력하세요.")
    inputData = input("문제 수를 다시 입력하세요")
total = int(inputData)


hit = 95
total = int(input("문제 수를 입력하세요"))
score = int(hit / total * 100)
print(f"{total}문제 중 {hit}문제를 맞추었으니 {score}점입니다.")


hit = 95
total = int(input("문제 수를 입력하세요"))
if total != 0:
    score = int(hit / total * 100)
    print(f"{total}문제 중 {hit}문제를 맞추었으니 {score}점입니다.")
else:
    print("입력된 문제의 수가 0입니다.")


try:
    hit = 95
    total = int(input("문제 수를 입력하세요"))
    score = int(hit / total * 100)
    print(f"{total}문제 중 {hit}문제를 맞추었으니 {score}점입니다.")
except:
    print("except:예외(exception)가 발생했어요")


listData = ["리눅스", "90", "파이썬", "자바", "90", "디비", "88"]
listScore = []
for score in listData:
    try:
        listScore.append(int(score))
    except:
        pass
print(f"listScore:{listScore}")


try:
    hit = 95
    total = int(input("문제 수를 입력하세요"))
    score = int(hit / total * 100)
    print(f"{total}문제 중 {hit}문제를 맞추었으니 {score}점입니다.")
except:
    print("except:예외(exception)가 발생했어요")
else:
    print("else:참 잘 했어요. 예외(exception)가 발생하지 않았어요.")
finally:
    print("finally:예외(exception)가 발생하든 하지않든 수고했어요")


gameResult = ["가위", "바위", "보", "종료"]
try:
    menuNumber = int(input("1.가위 2. 바위 3. 보 4. 종료 :"))
    result = gameResult(menuNumber - 1)
    print(f"입력하신 번호가 {menuNumber}이고, {result}를 냈습니다.")
except ValueError as exception:
    print("except ValueError:정수를 입력하세요")
    print(f"발생한 예외 : {exception}")
except IndexError as exception:
    print("except IndexError:0부터 2까지의 정수를 입력하세요")
    print(f"발생한 예외 : {exception}")
except NameError as exception:
    print("except NameError:Print()함수가 없습니다.")
    print(f"발생한 예외 : {exception}")
except Exception as exception:
    print("except Exception:예기치 못한 오류 발생")
    print(f"발생한 예외 : {exception}")


def getMenuNumber1():
    gameResult = ["가위", "바위", "보", "종료"]
    try:
        menuNumber = int(input("1.가위 2. 바위 3. 보 4. 종료 :"))
        result = gameResult(menuNumber - 1)
        print(f"입력하신 번호가 {menuNumber}이고, {result}를 냈습니다.")
    except ValueError as exception:
        print("except ValueError:정수를 입력하세요")
        print(f"발생한 예외 : {exception}")
    except IndexError as exception:
        print("except IndexError:0부터 2까지의 정수를 입력하세요")
        print(f"발생한 예외 : {exception}")
    except NameError as exception:
        print("except NameError:Print()함수가 없습니다.")
        print(f"발생한 예외 : {exception}")
    except Exception as exception:
        print("except Exception:예기치 못한 오류 발생")
        print(f"발생한 예외 : {exception}")
    finally:
        print("finally 발생")
    return


gameResult = ["가위", "바위", "보", "종료"]
menuNumber = getMenuNumber1()
while menuNumber != 4:
    result = gameResult[menuNumber - 1]
    print(f"입력하신 번호는 {menuNumber}이고, {result}를 냈습니다.")
    menuNumber = getMenuNumber1()


class MyClass:
    pass


myInstance1 = MyClass()


class MyClass:
    def whoAreYou(self):
        print(f"나는 {type(self)}의 객체입니다.")


myInstance1 = MyClass()
myInstance1.whoAreYou()


class MyClass:
    def __init__(self, name):
        self.name = name

    def whoAreYou(self):
        print(f"나는 {type(self)}의 객체 {self.name}입니다.")


myInstance1 = MyClass("MyClass object1")


class Cat:
    def __init__(self, name):
        self.name = name

    def whoAreYou(self):
        print(f"나는 {type(self)}의 객체 {self.name}입니다.")


class Dog:
    def __init__(self, name):
        self.name = name

    def whoAreYou(self):
        print(f"나는 {type(self)}의 객체 {self.name}입니다.")


tom = Cat("톰")
nero = Cat("네로")
badugi = Dog("바둑이")
dengDengi = Dog("댕댕이")
list1 = [tom, nero, badugi, dengDengi]
for item in list1:
    item.whoAreYou()


class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print(f"{self.name} : 야옹~ 야옹~")


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} : 멍멍~ 멍멍~")
