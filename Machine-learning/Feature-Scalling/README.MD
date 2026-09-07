# Feature Scalling
**That is, rescaling numerical features (columns) so that they fall within a comparable range or distribution, without losing the relative meaning of the data.**

**The goal** ``is to ensure that a column such as salary with values ​​in the tens of millions is not considered more important than a column such as age with a range of 18 to 70 simply because of its large number. ``

## When we need that?
It is usually important for distance-sensitive models, and models that are optimized by gradients.

- KNN : cause it calculates the distance between points
- K-Means : Because it forms clusters based on distance
- SVM : Because it depends on the distance and decision boundary
- PCA : Because it is sensitive to feature variance
- Neural Networks : For more stable training and faster convergence
- Logistic Regression and Linear Regression, especially with Regularization or Gradient Descent

**but is not usually important for tree's models**

- Decision Tree

- Random Forest

- XGBoost

- LightGBM

- CatBoost

## Technique

### Standardization
-> It transforms each value relative to the mean and standard deviation of the same column.

$$
x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

**good for :** 
`Logistic Regression, SVM, KNN, PCA, Neural Network and many linear models.`
​
### Min Max 
-> It usually takes the data into the range 0 to 1.

$$
x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$
​
++ **Pros**: Has a clear and understandable range 

-- **Weakness**: Very sensitive to outliers; if there is a very large abnormal return, most of the normal values ​​will be compressed near zero

**good for :**
``When you need a limited range, the data inherently has a lower and upper limit, or some neural networks.``

### Robust
-> This method uses the median and IQR instead of the mean and standard deviation; therefore, the effect of outliers is less.

$$
x' = \frac{x - \operatorname{median}(x)}{\operatorname{IQR}(x)}
$$
 
 **good for :**
 ``Columns like income, house price, or purchase amount that have serious outliers. Scaling doesn't remove the outlier itself; it just doesn't allow the scale to severely distort the entire column.``
​
### Normalization 