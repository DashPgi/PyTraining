from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()


iris.data # ->  Feature or X
iris.target # -> Target or Y
# test_size=0.2 -> 20% of the data will be used for testing, and 80% for training
# random_state=42 ->  Random seed for reproducibility
# stratify=y ->  Ensures that the proportion of each class is maintained in both training and testing sets