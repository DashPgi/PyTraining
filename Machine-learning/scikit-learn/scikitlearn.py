from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()


df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

print(df.head())
print("shapes", df.shape)
print("class name", iris.target_names)
# Classification

# Regression

# Model Selection