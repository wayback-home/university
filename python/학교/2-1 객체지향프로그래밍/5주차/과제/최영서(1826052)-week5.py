# 객체지향 프로그래밍 5주차 예제, 컴퓨터공학과 2학년 1826052 최영서

#
list1 = [1, 2, 3, 4, 5]
list2 = ["H", "e", "l", "l", "o"]
list3 = ["홍길동", "Python", 95, 4.5, True]

l = ["홍길동", "Python", 95, 4.5, True]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

#
list1 = [1, 2, 3, 4, 5]
print(list * 3)

l = ["H", "e", "l", "l", "o"]
print(len(l))
print(l[5])

hello = ["H", "e", "l", "l", "o"]
print(hello[1])
print(hello[2])
print(hello[-1])
print(hello[-0])
print(hello[-len(hello)])

#
list1 = [1, 2, 3, 4, 5]
print(list1[2:4])

print(list1[2:])
print(list1[:4])
print(list1[:])

#
list1 = [1, 2, 2, 3, 3, 3]
list1.count(2)
list1.count(3)

list1 = ["홍길동", "Python", 95, 4.5, True]
print(list1.count(80))
print(list1.count(95))
print(list1.count(True))

#
question = "I am happy!"
list1 = list(question)
print(list1)

list1 = ["I", " ", "a", "m", " ", "h", "a", "p", "p", "y", "!"]
print(list1.find("a"))
print(list1.index("?"))

#
question = "I am happy! Are you happy?"
list1 = question.split()
print(list1[1])

#
list1 = [1, 2, 3]
list1.append(4)

#
list1 = [1, 2, 3, 4, 5]
list1.insert(1, 0)
print(list1)

#
list1 = [1, 2, 3, 4, 5]
list1.remove(3)
print(list1)

#
list1 = ["홍길동", "Python", 95, 4.5, True]
print(list1)
list2 = list1.copy()
print(list2)

#
list1 = [1, 2, 3, 4, 5]
del list1[1]
print(list1)

list1 = [1, 2, 3, 4, 5]
del list1[2:4]
print(list1)

#
list1 = [1, 2, 3, 4, 5]
print(2 in list1)
print(6 in list1)
print(6 not in list1)

#
i = 0
list1 = []
for i in range(0, 10, 2):
    list1.append(i)
print(list1)

#
list1 = [1, 2, 3, 4]
for item in list1[:-1]:
    print(item)

#
list1 = [1, 2, 3, 4, 5]
reversedList1 = reversed(list1)
print(reversedList1)

#
list1 = ["H", "e", "l", "l", "o"]
for i in range(len(list1)):
    print(f"{i}번째 요소는 {list1[i]}입니다.")

#
list1 = ["H", "e", "l", "l", "o"]
print(enumerate(list1))
print(list(enumerate(list1)))

#
dict1 = {}
dict2 = dict()

dict1 = {1: "One"}
dict1[2] = "Two"
dict1[0] = "zero"
print(dict1)

#
dict1 = {"name": "KimOneTwo", type: "학생"}
del dict1[type]
print(dict1)

#
dict1 = {"name": "김박사", type: "교수", "강의과목": ["Python", "OS", "AI"]}
del dict1["강의과목"]
print(dict1)

#
dict1 = {"이름": "홍길동", "과목": "Python", "성적": 95, "평점": 4.5, "pass": True}
print(dict1.keys)
print(dict1.keys())

#
name = "name"
dict2 = {"name": "김박사", type: "교수", "강의과목": ["Python", "OS", "AI"]}
print(dict2.values())
print(dict2.values)

#
dict1 = {"이름": "홍길동", "과목": "Python", "성적": 95, "평점": 4.5, "pass": True}
print(dict1.items())

#
dict1.clear()
print(dict1)

#
dict1 = {"이름": "홍길동", "과목": "Python", "성적": 95, "평점": 4.5, "pass": True}
dict1.get("이름")
dict1.get("과목")

#
tuple1 = (1, 2, 3)
tuple1 = (1,)
print(type(tuple1))

#
tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3
tuple3 = ("a", 3.14, (1, 2, 3))
tuple4 = ("홍길동", "python", 95, 4.5, True)
tuple5 = ("h", "e", "l", "l", "o")

#
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[2:4])
print(tuple1[2:])
print(tuple1[:4])
print(tuple1[:])
print(tuple1[1:-1])

#
set1 = set([1, 2, 3])
print(set1)

#
set1 = set([1, 2, 3, 4, 5, 6])
set2 = set([4, 5, 6, 7, 8, 9])
print(set1 | set2)
print(set1.union(set2))

#
set1 = set([1, 2, 3, 4, 5])
set1.add6
print(set1)

set1 = set([1, 2, 3])
set1.update([4, 5, 6])
print(set1)

set1 = set([1, 2, 3, 4, 5])
set1.remove(3)
print(set1)
