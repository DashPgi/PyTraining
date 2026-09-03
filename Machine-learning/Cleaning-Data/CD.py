import pandas as pd

data = pd.read_csv("employees_dirty.csv")

# print(data.head())

# print(f"duplicated data = {data.duplicated(subset='email').sum()}")

# 5 columns hase a missing data [age,salary,experience,email,performance_score]
# print(data[data.isna().any(axis=1)])

data["age"] = data["age"].fillna(data["age"].mean())

data["salary"] = pd.to_numeric(data["salary"], errors="coerce")
data["salary"] = data["salary"].fillna(data["salary"].mean().round())

data["performance_score"] = data["performance_score"].fillna(
    data["performance_score"].mean().round()
)
data["email"] = data["email"].fillna("Unknown")
data["experience"] = data["experience"].fillna(
    data["experience"].median().round()
)
# print(data.isna().sum())

# Age and Experience and emid and performance_score

Q1 = data["age"].quantile(0.25)
Q3 = data["age"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

data = data[
    (data["age"] >= lower) &
    (data["age"] <= upper)
    ]

Q1 = data["experience"].quantile(0.25)
Q3 = data["experience"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
data = data[
    (data["experience"] > lower) & (data["experience"] < upper)
    ]

Q1 = data["performance_score"].quantile(0.25)
Q3 = data["performance_score"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
data = data[
    (data["performance_score"] >= lower) & (data["performance_score"] <= upper)
    ]

print(data.duplicated().any())
print(data.isna().sum())
print(data.std(numeric_only=True))
print(data.dtypes)
print((data["age"] < 0).sum())
print((data["age"] > 120).sum())
print((data["employee_id"] < 0).sum())
if not data["gender"].isin(["Male", "Female"]).all():
    print("gender error")