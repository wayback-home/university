tt1 = (10, 20, 30)
print(tt1)

tt2 = 40, 40, 60
print(tt2)

tt3 = 10
print(tt3)

tt4 = (10,)
print(tt4)

tt5 = (10,)
print(tt5)

print(tt1 + tt2)
print(tt1[1:3])
print(tt1 * 3)
# tt1.append(40) 튜플은 수정 불가

b = list(tt1)
print(b)

del tt1  # 튜플 전체 삭제는 가능/리스트처럼 내부 요소만 지우는것은 불가능
print(tt1)