# 객체지향 프로그래밍 4주차 예제 : 가위바위보 프로그램 작성, 컴퓨터공학과 2학년 1826052 최영서
import random
import sys
import time

if len(sys.argv) == 2 and sys.argv[1] == "/?":
    print("이 프로그램은 컴퓨터와 가위바위보를 하는 프로그램입니다.")
    print("프로그램을 실행할 경우 메뉴가 출력됩니다.")
    print("가위바위보가 끝나면 전체 실행 결과와 승률, 등급이 출력됩니다.")
    print("메뉴 열람")
    print("1.가위  2. 바위  3. 보  4. 종료")

else:
    # 이름을 받기
    userName = input("이름을 입력하세요 : ")
    # 승률 계산을 위한 변수 선언
    userWincount = 0
    comWincount = 0
    samecomuser = 0

    # 시간에 따른 인삿말을 다르게 하기 위해 time 모듈을 이용해 현재 local 시간을 변수로 선언
    timenow = time.localtime(time.time())
    gettime = timenow.tm_hour

    # 시간에 따른 인삿말 출력
    print("\n" * 30)
    if gettime <= 6:
        print(f"\t\t{userName}님.. 잠도 안자나요?")
    elif gettime <= 12:
        print(f"\t\t{userName}님! 반갑습니다.")
    elif gettime <= 18:
        print(f"\t\t{userName}님! 할일은 다 하셨나요?")
    else:
        print(f"\t\t{userName}님! 오늘 하루도 수고하셨습니다!")
    print("\n" * 3)

    # 가위바위보 연산
    print("\t가위바위보를 합시다~~~~ 가위바위보를 내세요")
    userResult = input("\t1.가위  2. 바위  3. 보  4. 종료  : ")
    while userResult not in ["1", "2", "3", "4"]:
        print("잘못 냈어요~ 정신좀 차리세요~~")
        userResult = input("\t1.가위  2. 바위  3. 보  4. 종료  : ")

    while userResult != "4":
        computerResult = random.randrange(3) + 1

        if computerResult == 1:
            if userResult == "1":
                print((f"\t{userName} : 가위   컴퓨터 : 가위"))
                print(f"\t{userName}님과 컴퓨터가 비겼습니다.")
                print("\t사이좋게 비겼네요~~")
                print("\n")
                samecomuser += 1

            elif userResult == "2":
                print((f"\t{userName} : 바위   컴퓨터 : 가위"))
                print(f"\t{userName}님이 컴퓨터를 이겼습니다.")
                print("\t감히 나를 이기다니...")
                print("\n")
                userWincount += 1

            elif userResult == "3":
                print((f"\t{userName} : 보   컴퓨터 : 가위"))
                print(f"\t{userName}님이 컴퓨터에게 졌습니다.")
                print("\t내가 이겼지롱~~~")
                print("\n")
                comWincount += 1

        elif computerResult == 2:
            if userResult == "1":
                print((f"\t{userName} : 가위   컴퓨터 : 바위"))
                print(f"\t{userName}님이 컴퓨터에게 졌습니다.")
                print("\t내가 이겼지롱~~~")
                print("\n")
                comWincount += 1

            elif userResult == "2":
                print((f"\t{userName} : 바위   컴퓨터 : 바위"))
                print(f"\t{userName}님과 컴퓨터가 비겼습니다.")
                print("\t사이좋게 비겼네요~~")
                print("\n")
                samecomuser += 1

            elif userResult == "3":
                print((f"\t{userName} : 보   컴퓨터 : 바위"))
                print(f"\t{userName}님이 컴퓨터를 이겼습니다.")
                print("\t감히 나를 이기다니...")
                print("\n")
                userWincount += 1

        elif computerResult == 3:
            if userResult == "1":
                print((f"\t{userName} : 가위   컴퓨터 : 보"))
                print(f"\t{userName}님이 컴퓨터를 이겼습니다.")
                print("\t감히 나를 이기다니...")
                print("\n")
                userWincount += 1

            elif userResult == "2":
                print((f"\t{userName} : 바위   컴퓨터 : 보"))
                print(f"\t{userName}님이 컴퓨터에게 졌습니다.")
                print("\t내가 이겼지롱~~~")
                print("\n")
                comWincount += 1

            elif userResult == "3":
                print((f"\t{userName} : 보   컴퓨터 : 보"))
                print(f"\t{userName}님과 컴퓨터가 비겼습니다.")
                print("\t사이좋게 비겼네요~~")
                print("\n")
                samecomuser += 1

        print("\n" * 35)
        print("\t가위바위보를 합시다~~~~ 가위바위보를 내세요")
        userResult = input("\t1.가위  2. 바위  3. 보  4. 종료  : ")
        while userResult not in ["1", "2", "3", "4"]:
            print("\t잘못 냈어요~ 정신좀 차리세요~~")
            userResult = input("\t1.가위  2. 바위  3. 보  4. 종료  : ")

    # 승률 계산
    count = int(userWincount + comWincount + samecomuser)  # 전체판수
    wincount = float(userWincount / count * 100)  # 승률

    # 등급 계산
    if wincount >= 90:
        grade = "A"
    elif wincount >= 80:
        grade = "B"
    elif wincount >= 70:
        grade = "C"
    elif wincount >= 60:
        grade = "D"
    else:
        grade = "F"

    # 승률 출력
    print("\n" * 30)
    print(
        "\t============================================================================"
    )
    print("\t  이름    이긴판수    진 판수    비긴판수    전체판수    승률    ")
    print(
        f"\t  {userName}  {userWincount}           {samecomuser}          {comWincount}           {count}           {wincount}%",
    )
    print(
        "\t============================================================================"
    )
    print(f"\t\t\t\t\t\t\t\t\t종합등급 : {grade}")

    if userWincount > comWincount:
        print("\t조만간 또 오세요~ 내가 가위바위보를 더 연습해 놓겠습니다")
    elif userWincount < comWincount:
        print("\t실력 좀 더 쌓은 후에 오세요~~~~~ 아직 내겐 멀었네요~")
    else:
        print("\t안녕히 가세요.")

    print("\n")