import pandas as pd
import numpy as np

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
