# Linear-regreession
**It is a method for predicting continuous values.**

Formula :
 $$ \hat{y} = \beta_0 + \beta_1 x $$

**Y** :  Predicted Value

**X** : Input value

**𝛽₀** : Y-intercept; the predicted value when x = 0

**𝛽₁** : Slope of the line; the rate of change in the output for a one-unit increase in the input : 

$$\beta_1 = \frac{y_2-y_1}{x_2-x_1} $$

## Multivariate linear regression

**If we possess a few variate** : 
$$
\hat{y} = \beta_0 + x_1\beta_1 + x_2\beta_2 + ... + x_n\beta_n
$$

### How Models Learn?

The model selects the $\beta$ coefficients such that the prediction line or plane is as close as possible to the actual data. Typically, the least squares criterion is used:

#### Mean Squared Error
$$
MSE = \frac1{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$
$$ OR $$
$$
MSE = \frac1{n}\sum_{i=1}^{n}e_i^2
$$

$$e_i = Error , Residual $$
we take the difference between the actual value and the predicted value and try to minimize it.

#### Mean Absolute Error

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y_i}|
$$

#### Root Mean Squared Erorr
$$
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y_i})^2}
$$

#### R2
$$
R^2 = 1-\frac{\sum_{i=1}^{n}(y_i-\hat{y_i})^2}
{\sum_{i=1}^{n}(y_i-\bar{y})^2}
$$

**The smaller and more patternless and more the Residual, the model is better**



### Common criteria

| Metric | Meaning | Better |
| ------ | ---------------------------------------------- | ------- |
| MAE    | Mean Absolute Error                            | Lower   |
| MSE    | Mean Squared Error; more sensitive to large errors | Lower   |
| RMSE   | Root MSE; in the target variable's original units | Lower   |
| R²     | Approximate percentage of output variation explained by the model | Closer to 1 |

## Tips

- **The relationship between inputs and outputs must be close to linear**
- **The observations must be Independent**
- **Homogeneity of variance**
- **The errors should not have a highly unusual distribution, especially if the goal is statistical analysis and hypothesis testing**
- **Multicollinearity**
- **Less Outliers**


## When is it not suitable?
**Linear regression is not a good choice if** :

- The output is categorical, such as "pass/fail" or "spam/not spam"; in this case, Logistic Regression is usually more appropriate.

- The relationship is highly non-linear and cannot be improved through feature transformation or the creation of new features.

- There are numerous outliers in the data.

- The output represents a count, such as the number of calls or accidents; count models like Poisson Regression might be more suitable.

# With python
```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X = df[["area", "bedrooms", "age"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
print("MAE:", mean_absolute_error(y_test, predictions))
print("MSE:", mean_squared_error(y_test, predictions))
print("R²:", r2_score(y_test, predictions))
```