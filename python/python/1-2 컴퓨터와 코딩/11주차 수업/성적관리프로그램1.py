#####################성적관리 프로그램#######################
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

score += [[0, 0, 0, 0, 0]]  # 2행 추가

for i in range(0, getPeople):
    for j in range(0, 3):
        score[i][3] += score[i][j]  # ..........학생의 개인별 총점
        score[getPeople][j] += score[i][j]  # ..과목별 총점
        score[getPeople][3] += score[i][j]  # ..모든 점수의 합

sumscore = 0  # 평균값을 구하기 위한 변수 선언/1.합계
perscore = 0  # 평균값을 구하기 위한 변수 선언/1.평균계산


for i in range(0, getPeople + 1):  # .. 리스트에서 총점을 빼서 상수계산, 평균값 산출
    sumscore = score[i][3]  # ......... 합계에서도 평균을 출력하도록 getPeople +1로 계산
    perscore = sumscore / 3  # ........ 합계에서의 평균은 과목별 총점의 평균을 계산
    score[i][4] = round(perscore, 2)

print("이름   국어     영어    수학    총점    평균")  # 테이블 출력


for i in range(0, getPeople + 1):
    if i < getPeople:
        print("%s" % name[i], end="   ")
    else:
        print("합계", end="  ")
    for j in range(0, 5):
        print("%5d" % score[i][j], end="   ")
    print()
