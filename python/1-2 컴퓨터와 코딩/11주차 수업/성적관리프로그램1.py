###########################################################
#######################성적관리 프로그램######################
############컴퓨터 정보기술 공학부 1826052 최영서##############
###################컴퓨터와 코딩 11주차 과제##################
###########################################################
#############1. 총점/ 2. 소숫점 둘째자리까지 평균##############
###########################################################
###########################################################


score = []
name = []

getPeople = int(input("성적을 받을 사람의 수 : "))  # 몇명의 성적을 받을지 결정하는 변수


for i in range(0, getPeople):
    getname = input("이름 입력 : ")
    name.append(getname)
    getscore = input("%s의 국어, 영어, 수학 점수 : " % name[i]).split()
    score.append(list(map(float, getscore)))
    score[i].append(0)
    score[i].append(0)

score += [[0, 0, 0, 0, 0]]  # 2행 추가/2차원 배열로 확장

for i in range(0, getPeople):
    for j in range(0, 3):
        score[i][3] += score[i][j]  # ..........학생의 개인별 총점
        score[getPeople][j] += score[i][j]  # ..과목별 총점
        score[getPeople][3] += score[i][j]  # ..모든 점수의 합

sumscore = int(0)  # .......평균값을 구하기 위한 변수 선언/1.합계
perscore = float(0)  # .....평균값을 구하기 위한 변수 선언/2.평균계산


print("이름   국어     영어    수학    총점    평균")  # 테이블 출력


for i in range(0, getPeople + 1):  # .......입력받은 사람 수보다 많은경우
    if i < getPeople:  # .......합계 테이블이 출력되도록 반복문 설정
        print("%s" % name[i], end="   ")

    else:
        print("합계", end="  ")

    for j in range(0, 4):  # 국어부터 총점까지의 점수 출력
        print("%5d" % score[i][j], end="   ")

        for k in range(0, getPeople + 1):  # 총점을 리스트에서 뽑아 평균값 계산
            sumscore = score[i][3]
            perscore = sumscore / 3  # .....국어, 영어, 수학 총 3과목이므로 /3으로 계산

    print("  %5.2f" % (perscore))  # 평균값 출력
