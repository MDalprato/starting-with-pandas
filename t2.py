import pandas as pd

titanic = pd.read_csv("titanic.csv")

# print(titanic)
# print(titanic.head(8))
# print(titanic.dtypes)

print(titanic.info())

ages = titanic["Age"]

print(ages.head())