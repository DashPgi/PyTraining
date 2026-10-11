import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("Chaos-data.csv")

X = data.drop("churn", axis=1)
y = data["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

X_train, X_temp, y_train, y_temp = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp,
    test_size=0.5,
    random_state=42
)

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)