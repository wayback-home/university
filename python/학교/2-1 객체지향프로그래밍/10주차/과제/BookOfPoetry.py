from Poetry import *


class BookOfPoetry(object):
    """description of class"""

    def __init__(self):
        self._poetryBook = list()

        title = "진달래 꽃"
        poet = "김소월"
        contents = """나 보기가 역겨워
가실 때에는
말없이 고이 보내 드리우리다

영변에 약산
진달래꽃
아름 따다 가실 길에 뿌리우리다

가시는 걸음 걸음
놓인 그 꽃을
사뿐히 즈려밟고 가시옵소서

나 보기가 역겨워
가실 때에는
죽어도 아니 눈물 흘리우리다"""

        myPoetry = Poetry(title, poet, contents.split("\n"))
        self._poetryBook.append(myPoetry)

        title = "그리움"
        poet = "유치환"
        contents = """오늘은 바람이 불고
나의 마음은 울고 있다
일찍이 너와 거닐고 바라보던
그 하늘 아래 거리언마는
아무리 찾으려도 없는 얼굴이여
바람 센 오늘은 더욱 너 그리워
진종일 헛되이 나의 마음은
공중의 깃발처럼 울고만 있나니
오오 너는 어디메 꽃같이 숨었느뇨"""

        myPoetry = Poetry(title, poet, contents.split("\n"))
        self._poetryBook.append(myPoetry)

        title = "먼 곳에서부터"
        poet = "김수영"
        contents = """먼 곳에서부터
먼 곳으로
다시 몸이 아프다
조용한 봄에서부터
조용한 봄으로
다시 내 몸이 아프다
여자에게서부터
여자에게로
능금꽃으로부터
능금꽃으로……
나도 모르는 사이에
내 몸이 아프다"""

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