# 객체지향 프로그래밍 14주차 예제, 컴퓨터공학과 2학년 1826052 최영서


from abc import *


class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def goToSchool(self):
        pass


class Student(StudentBase):
    def study(self):
        print("공부하는 중입니다.")

    def goToSchool(self):
        print("학교 가는 중입니다.")


gilDong = Student()
gilDong.study()
gilDong.goToSchool()


from abc import abstractmethod, ABCMeta


class Question(metaclass=ABCMeta):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def askTheUser(self):
        pass


class YesNoQuestion(Question):
    def __init__(self, text):
        Question.__init__(self, text)

    def askTheUser(self):
        print(self.text)
        print("Yes or No..?")


class FreeTextQuestion(Question):
    def __init__(self, text):
        Question.__init__(self, text)

    def askTheUser(self):
        print(self.text)
        print("Well..? What's the answer...?")


def getQuestion():
    Questions = list()
    Questions.append(YesNoQuestion("Are you happy?"))
    Questions.append(FreeTextQuestion("Why or Why not?"))
    return Questions


Questions = getQuestion()
for question in Questions:
    question.askTheUser()
    print()

from abc import ABC, ABCMeta, abstractmethod
from datetime import datetime
from Menu import Menu


class ILogger(ABC):
    __metaclass__ = ABCMeta

    @abstractmethod
    def WriteLog(self, message):
        pass


class FileLogger(ILogger):
    def __init__(self, path):
        self.path = path
        self.logFile = open(path, "w")

    def WriteLog(self, message):
        with open(self.path, "a") as myFile:
            myFile.Write(str(datetime.now()) + message + "\n")


class ConsoleLogger(ILogger):
    def __init__(self):
        pass

    def WriteLog(self, message):
        print(str(datetime.now()) + message)


class ClimateMonitor:
    def __init__(self, logger):
        self.logger = logger

    def start(self):
        temperature = input("온도를 입력해주세요 : ")
        while temperature != "":
            self.logger.WriteLog("\t현재온도 : " + temperature)
            temperature = input("온도를 입력해주세요 : ")


title = "어디에 로깅할까요?"
contents = ["파일(Mylog.txt)", "콘솔"]
myMenu = Menu(title, contents)
myMenu.print()
myMenu.getMenuNumber()
while not myMenu.isExit():
    if myMenu.MenuNumber == 1:
        fileName = input("로그 파일 이름을 입력하세요 : ")
        if fileName == "":
            fileName = "myLog.txt"
        monitor = ClimateMonitor(FileLogger(fileName))
        monitor.start()
    elif myMenu.MenuNumber == 2:
        monitor = ClimateMonitor(ConsoleLogger())
        monitor.start()
    else:
        print("메뉴 객체에서는 도달할 수 없습니다.")
    myMenu.print()
    myMenu.getMenuNumber()
print("안녕히 가세요")

from abc import ABC, ABCMeta, abstractmethod
from Menu import *


class Gamer(ABC):
    __metaclass__ = ABCMeta
    Winner = "없음"
    PlayList = ["가위", "바위", "보"]
    isGameOver = False

    def __init__(self, name):
        self._name = name
        self._playResult = ""

    @property
    def Name(self):
        return self._name

    @property
    def playResult(self):
        return self._playResult

    @playResult.setter
    def playResult(self, value):
        self._playResult = value

    @abstractmethod
    def play(self):
        pass

    def _getWinner(self, otherPlayer):
        if self.playResult == "가위":
            if otherPlayer.playResult == "가위":
                Gamer.Winner = "없음"
            elif otherPlayer.playResult == "바위":
                Gamer.Winner = otherPlayer.Name
            elif otherPlayer.playResult == "보":
                Gamer.Winner = self.Name

        if self.playResult == "바위":
            if otherPlayer.playResult == "가위":
                Gamer.Winner = self.Name
            elif otherPlayer.playResult == "바위":
                Gamer.Winner = "없음"
            elif otherPlayer.playResult == "보":
                Gamer.Winner = otherPlayer.Name

        if self.playResult == "보":
            if otherPlayer.playResult == "가위":
                Gamer.Winner = otherPlayer.Name
            elif otherPlayer.playResult == "바위":
                Gamer.Winner = self.Name
            elif otherPlayer.playResult == "보":
                Gamer.Winner = "없음"

    def printGameResult(self, otherPlayer):
        self._getWinner(otherPlayer)
        print("{0} : {1}".format(self.Name, self.playResult))
        print("{0} : {1}".format(otherPlayer.Name, otherPlayer.playResult))

        if Gamer.Winner == "없음":
            print("{0}님이 {1}님과 비겼습니다.".format(self.Name, otherPlayer.Name))

        elif Gamer.Winner == self.Name:
            print("{0}님이 {1}님을 이겼습니다.".format(self.Name, otherPlayer.Name))

        else:
            print("{0}님이 {1}님을 이겼습니다.".format(otherPlayer.Name, self.Name))

class Person(Gamer):
    def __init__(self, name="사용자"):
        super().__init__(name)
    def play(self):
        title = "가위바위보:"
        myMenu = Menu(title, Gamer.PlayList)
        myMenu.print()
        myMenu.getMenuNumber()

        if myMenu.menuNumber != myMenu.ExitNumber:
            self.playResult = Gamer.PlayList[myMenu.MenuNumber -1]
        else:
            Gamer.isGameOver = True

import random
class Computer(Gamer):
    def __init__(self, name="컴퓨터"):
        super().__init__(name)
    def play(self):
        self.playResult = random.choice(Gamer.PlayList)


ComputerPlayer = Computer("컴퓨터")
PersonPlayer = Person(input("이름을 입력해 주세요 : "))
PersonPlayer.play()
while(not Gamer.isGameOver):
    ComputerPlayer.play():
    ComputerPlayer.printGameResult(PersonPlayer)
    print()
    PersonPlayer.play()
print("안녕히 가세요")
