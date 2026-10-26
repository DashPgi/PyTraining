from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris = load_iris()


x = iris.data  # ->  Feature or X
y = iris.target # -> Target or Y

x_train,x_test,y_train,y_test = train_test_split(
    x, y, test_size=0.2, # -> 20% of the data will be used for testing, and 80% for training
    random_state=42, # ->  Random seed for reproducibility
    stratify=y # -> Ensures that the proportion of each class is maintained in both training and testing sets
)

# ---

Model = somemodel() # -> Create a model instance
Model.fit(x_train, y_train) # -> Train the model on the training data
Model.predict(x_test) # -> Make predictions on the test data
accuracy_score(y_test, y_pred) # -> Evaluate the model's performance by comparing the predicted labels with the true labels

# -- Data's
scaler = StandardScaler() # -> row's outlier / ( row's mean - value ) = new value
scaler.transform(data) # -> Change data with new data and feature that scaler learned
Linerregin.coef_ # -> Coefficient or Slope of a line
Linerregin.intercept_ # constant number or Intercept

mean_absolute_error(y_test, pred) # -> MAE
r2_score(y_test, pred) # -> r^2


# -- Validation

cross_val_score(mode) # -> cross Validation

grid = GridSearchCV(
    estimator=wineknn, # -> Impressive our model
    param_grid=param_grid, # -> the Parameters that must be trained
    cv=5,
    scoring='accuracy' # -> Comparing criterion
)

print(grid.best_params_) # -> Best parameter mixing
print(grid.best_score_) # -> mean of best validation's score
# -- Pipeline



