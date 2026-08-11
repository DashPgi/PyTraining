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