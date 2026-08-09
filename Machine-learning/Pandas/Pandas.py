import pandas as pd
import numpy as np

missing_value = ["", " ", "0.0"]
file = pd.read_csv("data.csv", na_values=missing_value) # -> Replacing mising file into NaN


file.fillna(axis=0,inplace=True,value=np.nan)
file.fillna(method = "ffill",axis=0,inplace=True) # -> Forward Fill out
file.fillna(method = "bfill",axis=0,inplace=True) # -> backgward Fill out
file.dropna(axis=0, how="any", inplace=True) # -> any => delete all row's have NaN | -> all =>Delete a row's have all Nan
# linear interpolation => y = (y1+(x-x1))*(|y2-y1|/x2-x1)
file.interpolate(method="linear", inplace=True)
file.interpolate(method="polynomial", inplace=True)

