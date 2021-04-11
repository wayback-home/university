# 객체지향 프로그래밍 6주차 과제 : 시 출력 프로그램 , 컴퓨터공학과 2학년 1826052 최영서
import time
import os
import menu


title = ["진 달 래  꽃", "초        혼", "엄마야누나야", "개   여   울"]

lyrics1 = [
    "나 보기가 역겨워",
    "가실 때에는",
    "말없이 고이 보내 드리우리다",
    "영변에 약산",
    "진달래꽃",
    "아름 따다 가실 길에 뿌리우리다",
    "가시는 걸음 걸음",
    "놓인 그 꽃을",
    "사뿐히 즈려밟고 가시옵소서",
    "나 보기가 역겨워",
    "가실 때에는",
    "죽어도 아니 눈물 흘리우리다",
]

lyrics2 = [
    "산산이 부서진 이름이여!",
    "허공 중에 헤어진 이름이여!",
    "불러도 주인 없는 이름이여!",
    "부르다가 내가 죽을 이름이여!",
    "심중에 남아 있는 말 한마디는",
    "끝끝내 마저 하지 못하였구나.",
    "사랑하던 그 사람이여!",
    "사랑하던 그 사람이여!",
    "붉은 해는 서산마루에 걸리었다.",
    "사슴의 무리도 슬피 운다.",
    "떨어져 나가 앉은 산 위에서",
    "나는 그대의 이름을 부르노라.",
    "설움에 겹도록 부르노라.",
    "설움에 겹도록 부르노라.",
    "부르는 소리는 비껴 가지만",
    "하늘과 땅 사이가 너무 넓구나",
    "선 채로 이 자리에 돌이 되어도",
    "부르다가 내가 죽을 이름이여!",
    "사랑하던 그 사람이여!",
    "사랑하던 그 사람이여!",
]

lyrics3 = ["엄마야 누나야 강변 살자", "뜰에는 반짝이는 금모래 빛", "뒷문 밖에는 갈잎의 노래", "엄마야 누나야 강변 살자"]

lyrics4 = [
    "당신은 무슨 일로",
    "그리합니까?",
    "홀로이 개여울에 주저앉아서",
    "파릇한 풀포기가",
    "돋아나오고",
    "잔물은 봄바람에 헤적일 때에",
    "가도 아주 가지는",
    "그러한 약속이 있었겠지요",
    "날마다 개여울에",
    "나와 앉아서",
    "하염없이 무엇을 생각합니다",
    "가도 아주 가지는",
    "않노라심은",
    "굳이 잊지 말라는 부탁인지요",
]


def printPoetry(menuNumber, title, name):
    while menuNumber != "5":
        if menuNumber == "1":
            os.system("cls")
            print("\t\t", title[0], "\n")
            print("\t\t\t\t", name, "\n")
            i = 0
            for i in range(0, len(lyrics1) - 1):
                print("\t", lyrics1[i])
                time.sleep(1)

        elif menuNumber == "2":
            os.system("cls")
            print("\t\t", title[1], "\n")
            print("\t\t\t\t", name, "\n")
            i = 0
            for i in range(0, len(lyrics2) - 1):
                print("\t", lyrics2[i])
                time.sleep(1)

        elif menuNumber == "3":
            os.system("cls")
            print("\t\t", title[2], "\n")
            print("\t\t\t\t", name, "\n")
            i = 0
            for i in range(0, len(lyrics3) - 1):
                print("\t", lyrics3[i])
                time.sleep(1)

        elif menuNumber == "4":
            os.system("cls")
            print("\t\t", title[3], "\n")
            print("\t\t\t\t", name, "\n")
            i = 0
            for i in range(0, len(lyrics4) - 1):
                print("\t", lyrics4[i])
                time.sleep(1)

        time.sleep(4)
        os.system("cls")
        menu.printMenu(programtitle, name, content.split("\n"))
        menuNumber = menu.getMenuNumber()

    os.system("cls")
    print("\n\n\n")
    print("\t\t프로그램을 종료합니다.")
    print("\t\t이용해 주셔서 감사합니다.")
    print("\n\n\n")


programtitle = "시 출력 프로그램"
name = "김소월"
content = """진 달 래  꽃
초        혼
엄마야누나야
개   여   울"""


menu.printMenu(programtitle, name, content.split("\n"))
menuNumber = menu.getMenuNumber()
printPoetry(menuNumber, title, name)
