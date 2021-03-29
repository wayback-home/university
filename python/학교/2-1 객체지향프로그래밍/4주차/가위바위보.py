import random


userWincount = 0
comWincount = 0


userName = input("이름을 입력하세요 : ")
print()
print("가위바위보를 합시다~~~~ 가위바위보를 내세요")
userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")
while userResult not in ["1", "2", "3", "4"]:
    print("잘못 냈어요~ 정신좀 차리세요~~")
    userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")

while userResult != "4":
    computerResult = random.randrange(3) + 1

    if computerResult == 1:
        if userResult == "1":
            print((f"{userName} : 가위   컴퓨터 : 가위"))
            print(f"{userName}님과 컴퓨터가 비겼습니다.")
            print("사이좋게 비겼네요~~")

        elif userResult == "2":
            print((f"{userName} : 바위   컴퓨터 : 가위"))
            print(f"{userName}님이 컴퓨터를 이겼습니다.")
            print("감히 나를 이기다니...")
            userWincount += 1

        elif userResult == "3":
            print((f"{userName} : 보   컴퓨터 : 가위"))
            print(f"{userName}님이 컴퓨터에게 졌습니다.")
            print("내가 이겼지롱~~~")
            comWincount += 1

    elif computerResult == 2:
        if userResult == "1":
            print((f"{userName} : 가위   컴퓨터 : 바위"))
            print(f"{userName}님이 컴퓨터에게 졌습니다.")
            print("내가 이겼지롱~~~")
            comWincount += 1

        elif userResult == "2":
            print((f"{userName} : 바위   컴퓨터 : 바위"))
            print(f"{userName}님과 컴퓨터가 비겼습니다.")
            print("사이좋게 비겼네요~~")

        elif userResult == "3":
            print((f"{userName} : 보   컴퓨터 : 바위"))
            print(f"{userName}님이 컴퓨터를 이겼습니다.")
            print("감히 나를 이기다니...")
            userWincount += 1

    elif computerResult == 3:
        if userResult == "1":
            print((f"{userName} : 가위   컴퓨터 : 보"))
            print(f"{userName}님이 컴퓨터를 이겼습니다.")
            print("감히 나를 이기다니...")
            userWincount += 1

        elif userResult == "2":
            print((f"{userName} : 바위   컴퓨터 : 보"))
            print(f"{userName}님이 컴퓨터에게 졌습니다.")
            print("내가 이겼지롱~~~")
            comWincount += 1

        elif userResult == "3":
            print((f"{userName} : 보   컴퓨터 : 보"))
            print(f"{userName}님과 컴퓨터가 비겼습니다.")
            print("사이좋게 비겼네요~~")

    print()
    print("가위바위보를 합시다~~~~ 가위바위보를 내세요")
    userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")
    while userResult not in ["1", "2", "3", "4"]:
        print("잘못 냈어요~ 정신좀 차리세요~~")
        userResult = input("1.가위  2. 바위  3. 보  4. 종료  : ")

if userWincount > comWincount:
    print("조만간 또 오세요~ 내가 가위바위보를 더 연습해 놓겠습니다")
elif userWincount < comWincount:
    print("실력 좀 더 쌓은 후에 오세요~~~~~ 아직 내겐 멀었네요~")
else:
    print("안녕히 가세요.")
