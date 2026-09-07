import numpy as np
import pandas as pd
import feature_engine as fe

data = pd.read_csv("raw_customer_dataset.csv")

data.isna().sum()
data.duplicated().sum()
data = data.drop_duplicates()


data['age'] = data['age'].median()