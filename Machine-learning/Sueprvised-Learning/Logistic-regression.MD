# Logistic-regression

**A supervised machine learning algorithm for Classifications - particularly binary classification.**

*this model is used for the probability of a sample belonging to a specific category*
*ForExample : (1,0) or (yes,no) or (spam,not spam)*

## Types
#### Binary Logistic Regression
 Two classes (0/1) — what we have discussed so far

#### Multinomial Logistic Regression
More than two classes (Softmax Regression)

#### Ordinal Logistic Regression
Ordered classes (low/medium/high)

## Fomula

$$
P(y=1\mid x)=\frac{1}{1+e^{-(w^Tx+b)}}
$$

### Sigmoid

$$
P(y=1\mid x)
$$
this means every output (y) depends on the input (x)

and output must be between 1 and 0

`like when y=1 , x should ....`

**ForExample**

```
P(y=1|x) = 0.82
* The model estimates the probability of this sample belonging to class 1 to be 82%.* 
```

### $y$

**Our target or output**
$$
y \in {0,1}
$$

### $x$

**Our input**

### $w$

**Our input's weights**
$$
w =
\begin{bmatrix}
w\_1 \\
w\_2 \\
w\_3
\end{bmatrix}
$$

### $w^2$

**Our Transposed input's weight**

**Dot Product** :

$w^Tx$ : $w\_1x\_1+w\_2x\_2+w\_3x\_3$

### $b$

**This is the bias or the intercept.**

### $e$

**Euler's number** : $e \approx 2.71828$

### $-(w^Tx+b)$

**The negative sign causes the value to be input into the exponential function.**

### Sigmoid Functions

$$
\sigma(z)=\frac{1}{1+e^{-z}}
$$
**It causes our output to fall within the range {0, 1}**
$$0 < \sigma < 1$$

## Decision Boundary

*This ensures the output falls within the range {0, 1} like $\sigma$*

Decision Boundary
Our model effectively creates a linear boundary in the feature space. For a threshold of 0.5, the decision boundary is where:

$$𝜎(𝑤ᵀ𝑥 + 𝑏) = 0.5 ⇒ 𝑤ᵀ𝑥 + 𝑏 = 0$$

This means all points satisfying 𝑤ᵀ𝑥 + 𝑏 = 0 lie on the boundary; one side represents Class 1, and the other represents Class 0

Example: If we have only one feature (hours of study), the decision boundary is a point on the x-axis (e.g., 5 hours). More than 5 hours → Pass; less → Fail

## Cost Function

In linear regression, we use Mean Squared Error (MSE); however, in logistic regression, **MSE becomes non-convex and disrupts optimization**

Instead, we use the binary cross-entropy cost function, which converges and is derived from the maximum likelihood principle.

For a single sample $((x^{(i)} y^{(i)}))$ :

$$
L\left(\hat{y}^{(i)}, y^{(i)}\right)
====================================

\begin{cases}
-\log\left(\hat{y}^{(i)}\right), & \text{if } y^{(i)} = 1 \\
-\log\left(1-\hat{y}^{(i)}\right), & \text{if } y^{(i)} = 0
\end{cases}
$$

which can be written as a single formula:

$$
L
=

-\left\[
y^{(i)}\log\left(\hat{y}^{(i)}\right)
\+
\left(1-y^{(i)}\right)
\log\left(1-\hat{y}^{(i)}\right)
\right]
$$

### For the entire dataset

The average over (m) examples:

$$
J(w,b)
======

-\frac{1}{m}
\sum\_{i=1}^{m}
\left\[
y^{(i)}\log\left(\hat{y}^{(i)}\right)
\+
\left(1-y^{(i)}\right)
\log\left(1-\hat{y}^{(i)}\right)
\right]
$$

```
help:)
```

## Training Algorithm

Initialization:

Initialize w and b randomly or to zero.

For each sample $i$:
$z^{(i)} = w^T x^{(i)} + b$
$\hat{y}^{(i)} = \sigma(z^{(i)})$

Cost calculation:

$$
J = -\frac{1}{m} \sum_{i=1}^{m}
\left[
y^{(i)} \log\left(\hat{y}^{(i)}\right)
+
\left(1-y^{(i)}\right)
\log\left(1-\hat{y}^{(i)}\right)
\right]
$$

Backward pass:

$$\frac{\partial J}{\partial w\_j} = \frac{1}{m} \sum (\hat{y}^{(i)} - y^{(i)}) x\_j^{(i)}$$
$$
\frac{\partial J}{\partial b}
=
\frac{1}{m}
\sum_{i=1}^{m}
\left(
\hat{y}^{(i)} - y^{(i)}
\right)
$$

Updates:

wⱼ := wⱼ - α ∂J/∂wⱼ

b := b - α ∂J/∂b

Iteration:

Repeat steps 2 through 5 for a specified number of iterations until the cost converges.
