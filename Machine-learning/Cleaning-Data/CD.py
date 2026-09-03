import pandas as pd

data = pd.read_csv("employees_dirty.csv")

print(data.head())
print(data.duplicated().any())
# print(f"duplicated data = {data.duplicated(subset='email').sum()}")

print(data.isna().sum()) # 5 columns hase a missing data [age,salary,experience,email,performance_score]
print(data[data.isna().any(axis=1)])

data["age"] = data["age"].fillna(data["age"].mean())

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")
data["salary"] = data["salary"].fillna(data["salary"].mean())

data["performance_score"] = data["performance_score"].fillna(
    data["performance_score"].mean()
)
data["email"] = data["email"].fillna("Unknown")
data["experience"] = data["experience"].fillna(
    data["experience"].median()
)
print(data.isna().sum())