from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()


df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# print(df.head())
# print("shapes", df.shape)
# print("class name", iris.target_names)

x = iris.data
y = iris.target

x_train,x_test,y_train,y_test = train_test_split(
    x, y, test_size=0.2,
    random_state=42,
    stratify=y
)
# Classification

# Regression

# Model Selection