from matplotlib import markers
import pandas as pd
import matplotlib.pylab as plt

data = pd.read_csv("./list.csv")


Gyeongi = data.loc[0]
Gangwon = data.loc[1]
Chungbuk = data.loc[2]
Chungnam = data.loc[3]
Jeonbuk = data.loc[4]
Jeonnam = data.loc[5]
Gyungbuk = data.loc[6]
Gyungnam = data.loc[7]

sumPop = (
    Gyeongi + Gangwon + Chungbuk + Chungnam + Jeonbuk + Jeonnam + Gyungbuk + Gyungnam
)

year = [
    "1992",
    "1993",
    "1994",
    "1995",
    "1996",
    "1997",
    "1998",
    "1999",
    "2000",
    "2001",
    "2002",
    "2003",
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
]

print(sumPop)
# totalPop = [0 for _ in range(0, len(year), 1)]
totalPop = list()
for i in range(1, 90, 3):
    totalPop.insert(int(i / 3), sumPop[i])

print(totalPop)

plt.plot(year, totalPop[:29], marker="*")
plt.xlabel("연도")
plt.ylabel("인구수")
plt.show()
