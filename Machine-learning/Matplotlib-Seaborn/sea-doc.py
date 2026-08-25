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
plt.legend(bbox_to_anchor=(1.05, 1), title="Linechart")

# -- Barplot :

titanic_df = sea.load_dataset("titanic")
titanic_df.head()

fig, ax = plt.subplots()

sea.barplot(data=titanic_df,
            errorbar=None,
            hue="sex",
            x="class", y="fare", ax=ax)

# -- Historgram :

sea.histplot(
    data=titanic_df,
    x="age",
    alpha=0.4,
    hue="alone",
    palette="Set1",
    kde=True,
)

# -- KDE :

sea.kdeplot(data=titanic_df,
            x="age",
            fill=True,
            hue="alone",
            palette="Set1",
            multiple="stack",
            ls="--",
            bw_adjust=0.1)

fig, ax = plt.subplots()

sea.kdeplot(
    data=titanic_df,
    x="age",
    y="fare",
    fill=True,
    levels=6,
    cmap="inferno",
    ax=ax,
)

# -- Rugplot :
sea.rugplot(
    data=titanic_df,
    x="age",
)

# -- Boxplot :

sea.boxenplot(
    data=titanic_df,
    x="class",
    y="fare",
    hue="sex",
    hue_order=["male", "female"],
    order=["First", "Second", "Third"],
    showfliers=False,
    palette="Set2",
)

# -- ScatterPlot :

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

sea.scatterplot(
    data=iris_df,
    x="petal_length",
    y="petal_width",
    ax=ax[0],
)
ax[0].set_title("Iris Petal")
ax[1].set_title("Iris Sepal")
sea.scatterplot(
    data=iris_df,
    x="sepal_length",
    y="sepal_width",
    hue="species",
    palette="Set2",
    ax=ax[1]
)

# -- ViolinPlot :

sea.violinplot(
    data=titanic_df,
    x='class',
    y='age',
    hue='sex',
    palette="Set2",
    inner="box",
    split=True,
    hue_order=["male", "female"],
    gap=0.1,
    linewidth=1,

    inner_kws={"box_width": 4},
)

# -- CountPlot :

fig, ax = plt.subplots()

sea.countplot(
    data=titanic_df,
    x="class",
    hue='sex',
    hue_order=["male", "female"],
    palette="Set2",
    ax=ax
)

# -- StripPlot:
sea.stripplot(
    data=titanic_df,
    x="class",
    y="fare",
    alpha=0.5,
    palette="Set2",
    hue="sex",
    jitter=True,
    dodge=True,

)

# -- HeatmapPlot :
corr = titanic_df.corr(numeric_only=True)

sea.heatmap(
    data=corr,
    annot=True,
    fmt="0.1g",
)

# -- SwarmPlot :

Tips_df = sea.load_dataset("tips")
sea.swarmplot(
    data=Tips_df,
    x="day",
    y="total_bill",
    hue="smoker",
    dodge=True,
)

# -- PointPlot :

sea.pointplot(
    data=Tips_df,
    x="day",
    y="total_bill",
)
