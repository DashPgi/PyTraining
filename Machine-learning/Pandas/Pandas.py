import pandas as pd
import numpy as np

taintanic = pd.read_csv("taintanic.csv")
children =taintanic.loc(taintanic["age"] < 15 , "name")
adult = taintanic.loc(taintanic["age"] >20 , "name")
old_citizen = taintanic.iloc[2:5,25:2]

