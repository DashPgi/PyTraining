import pandas as pd
import numpy as np

data = pd.read_csv('tsd.csv', comment=';').head()

# How Handle Time Series data
print(data)
data.rename(columns={"timestamp":"datatime"})
data["datatime"] = pd.to_datetime(data["datatime"])

min = data["datatime"].min()
max = data["datatime"].max()
data["month"] = data["datatime"].dt.month

