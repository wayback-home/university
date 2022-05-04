bream_length = [
    25.4,
    26.3,
    26.5,
    29.0,
    29.0,
    29.7,
    29.7,
    30.0,
    30.0,
    30.7,
    31.0,
    31.0,
    31.5,
    32.0,
    32.0,
    32.0,
    33.0,
    33.0,
    33.5,
    33.5,
    34.0,
    34.0,
    34.5,
    35.0,
    35.0,
    35.0,
    35.0,
    36.0,
    36.0,
    37.0,
    38.5,
    38.5,
    39.5,
    41.0,
    41.0,
]
bream_weight = [
    242.0,
    290.0,
    340.0,
    363.0,
    430.0,
    450.0,
    500.0,
    390.0,
    450.0,
    500.0,
    475.0,
    500.0,
    500.0,
    340.0,
    600.0,
    600.0,
    700.0,
    700.0,
    610.0,
    650.0,
    575.0,
    685.0,
    620.0,
    680.0,
    700.0,
    725.0,
    720.0,
    714.0,
    850.0,
    1000.0,
    920.0,
    955.0,
    925.0,
    975.0,
    950.0,
]

smelt_length = [
    9.8,
    10.5,
    10.6,
    11.0,
    11.2,
    11.3,
    11.8,
    11.8,
    12.0,
    12.2,
    12.4,
    13.0,
    14.3,
    15.0,
]
smelt_weight = [
    6.7,
    7.5,
    7.0,
    9.7,
    9.8,
    8.7,
    10.0,
    9.9,
    9.8,
    12.2,
    13.4,
    12.2,
    19.7,
    19.9,
]


#! 산점도 표현
import matplotlib.pylab as plt

plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel("length")
plt.ylabel("weight")
plt.show()

# #! 사이킷 런에서 이용하기 위해 데이터를 병합, 제작
# t_length = bream_length + smelt_length
# t_weight = bream_weight + smelt_weight
# fish_data = [[l, w] for l, w in zip(t_length, t_weight)]

# #! 지도학습을 위한 정답(타겟) 작성
# fish_target = [5] * 35 + [7] * 14  # * 도미 = 5, 빙어 = 7 으로 지정


# #! k-최근접 이웃
# from sklearn.neighbors import KNeighborsClassifier

# kn = KNeighborsClassifier()
# kn.fit(fish_data, fish_target)
# print(kn.score(fish_data, fish_target))


# #! 특정 값을 선택할 때 도미일 확률 (35/49와 동일)
# kn49 = KNeighborsClassifier(n_neighbors=49)
# kn49.fit(fish_data, fish_target)
# print(kn49.score(fish_data, fish_target))


# #! 특정 값을 넣었을때 도미인지 빙어인지 판별(ex 30, 600을 넣었을 때) 5 = 도미, 7 = 빙어
# result = kn.predict([[30, 600]])
# print(result)
