import numpy as np
import pandas as pd
import feature_engine as fe
import sklearn as sk

pd.set_option('display.max_columns', None)
data = pd.read_csv("raw_customer_dataset.csv")

data.isna().sum()
data.duplicated().sum()
data = data.drop_duplicates()


REF_DATE = pd.Timestamp("2025-01-01")
data["signup_date"] = pd.to_datetime(data["signup_date"])
data["last_purchase_date"] = pd.to_datetime(data["last_purchase_date"])


data["tenure_days"] = (REF_DATE - data["signup_date"]).dt.days
data["days_since_last_purchase"] = (REF_DATE - data["last_purchase_date"]).dt.days
data["signup_month"] = data["signup_date"].dt.month
data["signup_weekday"] = data["signup_date"].dt.weekday
data["signup_is_weekend"] = data["signup_weekday"].isin([5, 6]).astype(int)



data = data.drop(columns=["signup_date", "last_purchase_date"])


data["review_length"] = data["product_review"].fillna("").str.len()
data["review_word_count"] = data["product_review"].fillna("").str.split().apply(len)
data["has_review"] = data["product_review"].notna().astype(int)
data = data.drop(columns=["product_review"])

data['age'] = data['age'].median()