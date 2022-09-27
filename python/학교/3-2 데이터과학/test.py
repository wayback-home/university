import pandas as pd
import requests
import io

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
s = requests.get(url, verify=False).content

names = [
    "sepal length in cm",
    "sepal width in cm",
    "petal length in cm",
    "petal width in cm",
    "species",
]


df = pd.read_csv(io.StringIO(s.decode("utf-8")), names=names)
print(df.head())
