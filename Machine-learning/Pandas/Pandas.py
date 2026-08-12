import pandas as pd
import numpy as np

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
