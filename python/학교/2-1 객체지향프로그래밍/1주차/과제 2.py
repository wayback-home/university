# 객체지향 프로그래밍 1주차 예제 : 시 출력 프로그램 작성, 컴퓨터공학과 2학년 1826052 최영서


import sys
import time

if sys.argv[1] == "/?":
    print("\n")
    print("이 프로그램은 노래의 가사를 재생합니다.")
    print("\n")
    print("노래 제목 : Celbrity")
    print("     가수 : IU")
    print("   작곡가 : Chloe Latimer, IU")
    print("앨범 정보 : 정규 5집 선공개")
    print("\n\n")

else:
    print("\n" * 30)

    lyrics = [
        "세상의 모서리",
        "구부정하게 커버린",
        "골칫거리 outsider",
        "걸음걸이, 옷차림",
        "이어폰 너머 playlist",
        "음악까지 다 minor",
        "넌 모르지 떨군 고개 위",
        "환한 빛 조명이 (어딜 비추는지)",
        "느려도 좋으니 결국 알게 되길",
        "The one and only,",
        "you are my celebrity",
        "잊지마 넌 흐린 어둠 사이",
        "왼손으로 그린 별 하나",
        "보이니 그 유일함이 얼마나",
        "아름다운지 말야",
        "You are my celebrity",
        "Celebrity",
        "You are my celebrity",
        "지쳐버린 표정 마치 전원을 꺼놓은 듯이",
        "심장소린 too quiet",
        "네가 가진 반짝거림",
        "상상력, identity",
        "까지 모조리 diet",
        "넌 모르지 아직 못다 핀",
        "널 위해 쓰여진 (오래된 사랑시)",
        "헤매도 좋으니 웃음 짓게 되길",
        "The one and only,",
        "you are my celebrity",
        "잊지마 넌 흐린 어둠 사이",
        "왼손으로 그린 별 하나",
        "보이니 그 유일함이 얼마나",
        "아름다운지 말야",
        "You are my celebrity",
        "발자국마다 이어진 별자리",
        "그 서투른 걸음이",
        "새겨놓은 밑그림",
        "오롯이 너를 만나러 가는 길",
        "그리로 가면 돼 점선을 따라",
        "잊지마 이 오랜 겨울 사이",
        "언 틈으로 피울 꽃 하나",
        "보이니 하루 뒤 봄이 얼마나",
        "아름다울지 말야",
        "You are my celebrity",
        "Celebrity",
        "You are my celebrity",
    ]
    for i in range(0, 45):
        print(lyrics[i])
        time.sleep(1)