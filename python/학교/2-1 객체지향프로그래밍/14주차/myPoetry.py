# 객체지향 프로그래밍 14주차 예제, 시 출력 프로그램, 컴퓨터공학과 2학년 1826052 최영서

from Menu import *
from Poetry import *


class BookOfPeotry(object):
    def __init__(self):
        self._poetrybook = list()
        self._getPoetry()

    @property
    def PoetryBook(self):
        return self._poetrybook

    def _getPoetry(self):
        fileName = "/mnt/c/Users/dudtj/study/ubuntu/python/학교/2-1 객체지향프로그래밍/14주차/myPoetryBook.txt"
        self._path = fileName
        title = ""
        poet = ""
        contents = list()
        isFirst = True
        with open(self._path, "r", encoding="UTF-8") as myFile:
            myBook = myFile.read().split("\n")
            for line in myBook:
                if line.startswith("제목"):
                    if isFirst:
                        isFirst = False
                    else:
                        myPoetry = Poetry(title, poet, contents)
                        self._poetrybook.append(myPoetry)
                        contents = []
                elif line.startswith("저자"):
                    poet = line[3:]
                else:
                    contents.append(line)

    def addPoetryBook(self, myPoetry):
        if myPoetry is None:
            return
        else:
            self._poetrybook.append(myPoetry)
