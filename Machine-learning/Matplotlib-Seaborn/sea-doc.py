import numpy as np
import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

# -- LinePlot :

df = sea.load_dataset("flights")

sea.lineplot(
    data=df,
    x="year",
    y="passengers",
    hue="month",
    palette="colorblind",
)
plt.legend(bbox_to_anchor=(1.05, 1),title="Linechart")

# -- Barplot :

titanic_df = sea.load_dataset("titanic")
titanic_df.head()

fig, ax = plt.subplots()

sea.barplot(data=titanic_df,
            errorbar=None,
            hue="sex",
            x="class", y="fare", ax=ax)

