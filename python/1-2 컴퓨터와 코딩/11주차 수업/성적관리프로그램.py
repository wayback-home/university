###성적관리 프로그램
score = []
name = []

for i in range(0, 3):
    tmp = input("이름 입력 : ")
    name.append(tmp)
    tmp2 = input("%s의 국어, 영어, 수학 점수 : " % name[i]).split()
    score.append(list(map(int, tmp2)))
    score[i].append(0)

score += [[0, 0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        score[i][3] += score[i][j]  ##학생의 개인별 총점
        score[3][j] += score[i][j]  ##과목별 총점
        score[3][3] += score[i][j]  ##모든 점수의 합

print("이름   국어    영어     수학    총점")


for i in range(0, 4):
    if i < 3:
        print("%s" % name[i], end="   ")
    else:
        print("합계", end="   ")
    for j in range(0, 4):
        print("%5d" % score[i][j], end="   ")
    print()
