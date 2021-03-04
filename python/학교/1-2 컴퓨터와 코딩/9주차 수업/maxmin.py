a, b, c = map(int,input("세 개의 숫자 입력 :").split())

if a>b :
    if a>c:
        max = a
    else :
        max = c
else :
    if b>c:
        max = b
    else : max = c

if a>b :
    if b>c :
        min = c
    else :
        min = b
else :
    if a>c :
        min = c
    else :
        min = a

print("최댓값은",max,"이고, 최솟값은",min,"입니다.")
