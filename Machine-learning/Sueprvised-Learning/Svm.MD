# Svm
**Support vector machine**

One of the most important algorithm for classification,regression and recognization outliers .

### Concept
The concept is finding the boundary with the maximum possible distance **($Margin$)**

### How does work?
Suppose we have datasets that any samples are belong between two class :
$$y_i \in \{-2,+2\}$$
And each of samples have multiple feature :
$$x_i = x,...,x_{i2},x_{i1}$$
And in the simplest case , we want find a line our plane that seprate two class :
$$b + w^Tx = 0$$
---
In two dimension,This equation is a line:
$$x_1 w_2+x_2w_2+b=0$$
In three dimension,this is a plane and in higher dimensions call that **hyperplane**

### SVM Function
$$b+w^Tx = f(x)$$

**Final prediction** : 
$$\hat{y} = \begin{cases}+1 & \text{if} f(x) >0 \\ -1 & \text{if}f(x) <0 \end{cases}$$
$\rightarrow final-decision :$
$$b+w^Tx = 0$$

## What is support vector?
The points that closer to decision border and marginal border 

$if \rightarrow$ We remove points far from the border $\rightarrow$ it is possible that the model not change

$but-if \rightarrow$ We remove SV $\rightarrow$ The model may change

**In Ideally way**, the boundary limits are as follows:
$$b+w^Tx = +1$$
$$and$$
$$b+w^Tx = -1$$

The decision boundary between them :
$$b+w^Tx = 0$$
The distance between two marginal boundaries is equal to :
$$
\frac{x}{\|w\|}
$$

Therefore, **if we want to maximize the margin, we must minimize ∥w∥** :
$$w\|min \frac{1}{2}|\ ^2$$ 
For this model ,we call it **Hard-Margin SVM**

## Hard Margin
In Hard-Margin SVM, we assume:

- The data are perfectly separable

- There is no noise

- No sample lies on the wrong side

- All samples must lie outside the margin

Optimization problem:
$$
\min_{w,b} \frac{1}{2}\|w\|^2
$$
But this way **isn't good for real world** cause : 
- Datas have noise 
- Datas have overlap
- Datas have outliers
- Datas are not completely detachable

For this situation we use Soft-Margin SVM

## Soft Margin
In Soft-Margin SVM, we allow some samples to:

- Fall within the margin

- Even be misclassified

To do this, we add variables $\xi_i$, which we call slack variables :
 $$
y_i\left(w^T x_i + b\right) \geq 1 - \xi_i
$$
### Goal's Function : 
$$
\min_{w,b,\xi}
\frac{1}{2}\|w\|^2
+
C\sum_{i=1}^{n}\xi_i
$$
Here, C is very important.

#### The Concept of Parameter C
Parameter C determines the balance between two objectives:

- A large margin

- Low training errors

*In Scikit-learn documentation, C is described as a parameter that balances the penalty for errors against the simplicity of the decision boundary*

$If$ **C is large**:
The model penalizes training errors more heavily

Typical result:

- Smaller margin.

- Greater effort to correctly classify training data.

- Higher sensitivity to noise.

- Higher risk of overfitting.

$If$ **C is small**:
The model is more tolerant of errors

Typical result:

- Larger margin

- Simpler model

- Greater robustness against noise

- Higher risk of underfitting

#  Hinge Loss
Another formula for understanding SVM : 
$$
L(y, f(x)) = \max(0, 1 - yf(x))
$$

So $\rightarrow$ :
$$f(x)=w 
T
 x+b$$

### Senrios
#### First Senario :
A completely correct sample, well away from the margin : 
$$If \rightarrow yf(x)≥1$$
$$Then \rightarrow L = 0$$
#### Second Senario :
The example is correct, but it falls within the margin :
$ If \rightarrow 0 < yf(x) < 1 $$
$$Then \rightarrow L>0$$
$Then \rightarrow $ the loss is positive, because the sample is correct but too close to the boundary

#### Third Senario :
$$If \rightarrow yf(x)<0$$
$$ Then \rightarrow L > 1$$

Thus, SVM does not focus solely on misclassified samples; it also penalizes samples that are correctly classified but lie close to the boundary

$$
\min_{w,b}
\frac{1}{2}\|w\|^2
+
C\sum_{i=1}^{n}
\max\left(0, 1-y_i\left(w^T x_i+b\right)\right)
$$

- The first part is regularization, which keeps the model simple

- The second part is the hinge loss

# Linear SVM
If the data can be separated approximately by a line or hyperplane, we use a linear SVM 
# Multi Class SVM
SVM was originally designed for binary classification, but methods such as these are used for multi-class classification :
## One vs One
A model is trained for each pair of classes 
If we have *k* class :
$$\frac{k(k-1)}{2}$$
## One vs Rest
For each class, we build a model that pits that class against all other classes

## Advantages of SVM
SVM is highly effective in the following scenarios:

- There is a large number of features

- The number of samples is moderate

- The boundary between classes is clear or modelable

- The data has been prepared with appropriate scaling

- Kernel-based models are required

### Key advantages:

- Ability to create linear and non-linear boundaries

- Strong performance in high-dimensional spaces

- Use of support vectors rather than relying directly on all data points

- Complexity control via the C parameter and kernels

- Suitable for both classification and regression

## Disadvantages of SVM
SVM is not always the best choice

Key disadvantages:

- It can be slow on very large datasets

- Selecting C, gamma, and the kernel requires experimentation

-  It is sensitive to feature scaling

-  Non-linear models are difficult to interpret

- It may overfit in the presence of significant noise if settings are inappropriate

- Additional processing is required to obtain probability estimates

- When the number of samples is very large, models such as Logistic Regression, SGD, or tree-based methods may be more suitable
