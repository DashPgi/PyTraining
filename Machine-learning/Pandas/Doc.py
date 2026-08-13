import pandas as pd

# Column's -> Series
# Header -> array[C,0]
# Label -> array[0,R]
# 1 - what kind of data does pandas handle? DataFrame's [ Tabular data ]


tabel = pd.DataFrame(
    {
        "name": ["parsa", "amir", "javad"],
        "age": [21, 23, 30],
        "sex": ["male", "male", "trans"]
    }
)

array = pd.DataFrame(

    np.random.default_rng(seed=1).integers(low=0, high=10, size=(2, 3)),
    columns=["esm", "famil", "age"],
    index=["a", 2]
)

Nationality = pd.Series(["Iranian", "Iranian", "Arab"], name="Nationality")
randomage = pd.Series(np.random.default_rng(seed=1).integers(low=0, high=255, size=10))

print(array.describe(include="all"))  # -> For all
print(array.describe(include="object"))  # -> For Str
print(array.describe(include="number"))  # -> For int
print(randomage)
print(tabel["name"])
print(f"Maximum number : {tabel['age'].max()}")
print(Nationality)
print(tabel.describe())
print(tabel["age"].sum())

# argmin & argmax in numpy == idxmin & idxmax in pandas

# 2 - How do I read and write tabular data?
# dataset = json,csv,iris

iris = pd.read_csv("iris.csv")
print(iris.head(), iris.tail())
iris.assign(newSeries="selected Series Or New Content")  # -> add new Column's in iris's DataFrame
iris.query("Series : filter")
iris.plot(kind="scatter", x="a Series", y="another Series")  # ->  for Diagram

data = pd.DataFrame()
data.to_csv("data.csv")
data.to_json("data.json")

# 3 - How do i select a subset of a DataFrame?

missing_value = ["", " ", "0.0"]
file = pd.read_csv("data.csv", na_values=missing_value) # -> Replacing mising file into NaN


file.fillna(axis=0,inplace=True,value=np.nan)
file.fillna(method = "ffill",axis=0,inplace=True) # -> Forward Fill out
file.fillna(method = "bfill",axis=0,inplace=True) # -> backgward Fill out
file.dropna(axis=0, how="any", inplace=True) # -> any => delete all row's have NaN | -> all =>Delete a row's have all Nan
# linear interpolation => y = (y1+(x-x1))*(|y2-y1|/x2-x1)
file.interpolate(method="linear", inplace=True)
file.interpolate(method="polynomial", inplace=True)


taintanic = pd.read_csv("taintanic.csv")
children =taintanic.loc(taintanic["age"] < 15 , "name")
adult = taintanic.loc(taintanic["age"] >20 , "name")
old_citizen = taintanic.iloc[2:5,25:2]
# groupby
data = {
    "Team": ["Iran", "Spain", "France", "USA", "Israel", "German"],
    "Rank": [9999, 1, 2, 3, 4, 5, ],
    "Year": [2014, 2020, 2026, 2025, 2020, 2005]
}
df = pd.DataFrame(data)
# df.style.hide_index() # hiding index
print(df)
# First step on group by (Split)
javad = df.groupby("Team").groups
print(javad.get_groups("iran"))

# Second step on groupby (function's) [Aggregation,transformation,filteration]
#   agg
print(javad["Year"].size())
print(javad["Year"].agg([np.sum]))
#   transformation
score = lambda x: (x - x.mean()) / x
print(df.transform(score))
#   filteraion
print(df.filter(lambda x : len(x) >= 3))


import matplotlib.pyplot as plt

# Virtualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Virtualization

data_GDP = {
    'Country' : ["Iran","USA","German","China"],
    'GDP' : [0.3,32,5,20]
}
plt.show()

GDP = pd.DataFrame(data_GDP,columns= ["Country","GDP"])
GDP.plot(x='Country',y='GDP', kind='bar')
print(GDP)
population = {
    "Iran": 2,
    "USA": 10,
    "Germany": 9,
    "China": 7
}

RankPop = pd.DataFrame(
    list(population.items()),
    columns=["country", "Score"]
)

print(RankPop)

RankPop.plot.pie(
    y="Score",
    labels=RankPop["country"],
    figsize=(5, 5),
    autopct="%.1f%%",
    startangle=90
)

plt.ylabel("")
plt.show()

# ---- need more doc for that

# How Creat new columns and calculate summary statistics

data = pd.read_csv('data.csv').head()

data["scale"] = data["Calories"] / 10
data = data.rename(
    columns={
        "Calories": "Cal"
    }
)
# Reshape the layout

pivot = data.pivot(columns="Pulse", values="Cal")
pivott = data.pivot_table(
    values="Cal",
    columns="Pulse",
    index="scale",
    aggfunc="mean"
)
malted = data.melt(id_vars="Pulse")
print(pivott)

