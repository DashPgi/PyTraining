# Logistic-regression

**A supervised machine learning algorithm for Classifications - particularly binary classification.**

*this model is used for the probability of a sample belonging to a specific category*
*ForExample : (1,0) or (yes,no) or (spam,not spam)*

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

$w^Tx$ : $w_1x_1+w_2x_2+w_3x_3$

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