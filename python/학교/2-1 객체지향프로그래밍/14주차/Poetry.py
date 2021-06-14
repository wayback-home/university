import os
import time


class Poetry(object):
    """description of class"""

    def __init__(self, title, poet, contents):
        self._title = title
        self._poet = poet
        self._contents = contents
        self._interval = 1

    @property
    def Title(self):
        return self._title

    def _printCLS(self):
        print("\n" * 30)

    def _printTitle(self):
        print("\t\t", end="")
        print(self._title)
        time.sleep(self._interval)

    def _printPoet(self):
        print("\t\t\t\t", end="")
        print(self._poet)
        time.sleep(self._interval)
        print()
        time.sleep(self._interval)

    def _printContents(self):
        for content in self._contents:
            print("\t", end="")
            print(content)
            time.sleep(self._interval)

    def _printBlankLine(self):

        for i in range(24 - len(self._contents)):
            print()
            time.sleep(self._interval)
        input("감상이 끝났으면 아무 키나 누르세요~~")

    def print(self):
        self._printCLS()
        self._printTitle()
        self._printPoet()
        self._printContents()
        self._printBlankLine()
