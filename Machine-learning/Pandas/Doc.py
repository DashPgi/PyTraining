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
