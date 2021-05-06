from Poetry import *


class BookOfPoetry(object):
    """description of class"""

    def __init__(self):
        self._poetryBook = list()

        title = "진달래 꽃"
        poet = "김소월"
        contents = """나보기가 역겨워 가실 때에는
        말없이 고이 보내드리우리다

        나보기가 역겨워 가실 때에는
        말없이 고이 보내드리우리다

        나보기가 역겨워 가실 때에는
        말없이 고이 보내드리우리다"""

        myPoetry = Poetry(title, poet, contents.split("\n"))
        self._poetryBook.append(myPoetry)

        title = "그리움"
        poet = "유치환"
        contents = """파도야 어쩌란 말이냐
        파도야 어쩌란 말이냐
        파도야 어쩌란 말이냐
        
        파도야 어쩌란 말이냐
        파도야 어쩌란 말이냐
        파도야 어쩌란 말이냐"""

        myPoetry = Poetry(title, poet, contents.split("\n"))
        self._poetryBook.append(myPoetry)

        title = "먼 곳에서부터"
        poet = "김수영"
        contents = """먼 곳에서부터
        먼 곳으로
        다시 내 몸이 아프다
        
        먼 곳에서부터
        먼 곳으로
        다시 내 몸이 아프다
        
        먼 곳에서부터
        먼 곳으로
        다시 내 몸이 아프다"""

        myPoetry = Poetry(title, poet, contents.split("\n"))
        self._poetryBook.append(myPoetry)

    @property
    def Poetry(self, menuNumber):
        return self._poetryBook[menuNumber - 1]

    @property
    def PoetryBook(self):
        return self._poetryBook

    @property
    def Length(self):
        return len(self._poetryBook)