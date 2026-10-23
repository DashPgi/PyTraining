from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()


x = iris.data  # ->  Feature or X
y = iris.target # -> Target or Y

x_train,x_test,y_train,y_test = train_test_split(
    x, y, test_size=0.2, # -> 20% of the data will be used for testing, and 80% for training
    random_state=42, # ->  Random seed for reproducibility
    stratify=y # -> Ensures that the proportion of each class is maintained in both training and testing sets
)


