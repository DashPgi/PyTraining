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
$$
MSE = \frac1{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$
$$ OR $$
$$
MSE = \frac1{n}\sum_{i=1}^{n}e_i^2
$$

$$e_i = Error , Residual $$
we take the difference between the actual value and the predicted value and try to minimize it.

**The smaller and more patternless and more the Residual, the model is better**

## Tips

- **The relationship between inputs and outputs must be close to linear**
- **The observations must be Independent**
- **Homogeneity of variance**
- **The errors should not have a highly unusual distribution, especially if the goal is statistical analysis and hypothesis testing**
- **Multicollinearity**
- **Less Outliers**