from pyexpat import model
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
import numpy as np


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



# KNN

Modelknn = KNeighborsClassifier(n_neighbors=3)

Modelknn.fit(x_train,y_train)

predict = Modelknn.predict(x_test)

accknn = accuracy_score(y_test,predict)

# Tree

Modeltree = DecisionTreeClassifier(max_depth=3)
Modeltree.fit(x_train,y_train)
predict = Modeltree.predict(x_test)
acctree = accuracy_score(y_test,predict)

# print(f"knn's accuracy: {accknn}")
# print(f"tree's accuracy: {acctree}")

datasets = np.ndarray([3,2])
scaler = StandardScaler()
scaler.transform(datasets)
scaled = scaler.fit_transform(datasets)


data = np.array([[25, 30],
                 [40, 80],
                 [60, 150]])

scaler = StandardScaler()
scaler.fit(data)

print("میانگین‌ها:", scaler.mean_)
print("انحراف معیارها:", scaler.scale_)

new_person = np.array([[40, 80]])
print("بعد از تبدیل:", scaler.transform(new_person))


# Classification

# Regression

# Model Selection