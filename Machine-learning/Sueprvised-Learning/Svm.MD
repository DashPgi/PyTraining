# Svm
**Support vector machine**

One of the most important algorithm for classification,regression and recognization outliers .

### Concept
The concept is finding the boundary with the maximum possible distance

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