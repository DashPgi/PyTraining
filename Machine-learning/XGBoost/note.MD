# XGBoost
### eXtreme Gradient Boosting

Is the powerful algorithm and python's library 
Best and fastest way for train Gradient Boosted Decision Trees Model

**For** :
- Regression 
- Classification 
- Ranking systems

## Concept : 
It trains several relatively simple decision trees in sequence, with each new tree attempting to correct the errors of the previous ones

In **Bagging/Random Forest**, trees are constructed largely independently and in parallel, and their results are combined via averaging or voting. In **Boosting**, however, models are built sequentially :

### 1. It builds a simple initial model

### 2. It examines the errors of that model

### 3. It trains the next model to perform better on those specific errors

### 4. It repeats this process

### 5. Ultimately, the final prediction is the sum of the contributions from all the trees

$Formula :$

$$
\hat{y}_i=\sum_{k=1}^{K} f_k(x_i)
$$