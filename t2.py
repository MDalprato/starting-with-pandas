import pandas as pd

titanic = pd.read_csv("titanic.csv")

# print(titanic)
# print(titanic.head(8))
# print(titanic.dtypes)


above_35 = titanic[titanic["Age"] < 3]

print(above_35.head())