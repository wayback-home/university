import pandas as pd


data = pd.read_csv(
    "/Users/choeyeongseo/Documents/ubuntu/python/학교/3-1 기계학습/week3/sample.csv"
)

OS = data["운영체제"]
Logic = data["논리회로"]
DB = data["DB"]

sum = OS + Logic + DB
avg = sum / 3

score = [0 for _ in range(0, len(avg), 1)]

for i in range(0, len(avg), 1):
    if avg[i] >= 90:
        score[i] = "A"
    elif avg[i] >= 80:
        score[i] = "B"
    else:
        score[i] = "C"


data.insert(4, "총점", sum)
data.insert(5, "평균", avg)
data.insert(6, "학점", score)


data_sorted = data.sort_values(axis=0, by="총점", ascending=False)

print(data_sorted)
