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


# Advantage :

High speed and scalability, even with big data

Support for CPU and GPU, and a scikit-learn-compatible interface

Built-in regularization to reduce overfitting

Relatively good handling of missing values

Feature Importance

Data Categorical

| Parameter        | Role                                   | Effect of Increasing the Value                                             |
| ---------------- | -------------------------------------- | -------------------------------------------------------------------------- |
| n_estimators     | Number of trees                        | Generally improves accuracy, but increases the risk of overfitting and training time |
| learning_rate    | Step size for error correction         | A smaller value is usually more stable, but requires more trees            |
| max_depth        | Depth of each tree                     | Deeper trees capture more complex patterns but are prone to overfitting    |
| min_child_weight | Minimum weight of samples in a leaf    | A larger value makes the model more conservative                           |
| subsample        | Proportion of samples used per tree    | Values ​​< 1 introduce randomness and improve resistance to overfitting      |
| colsample_bytree | Proportion of features used per tree   | Values ​​< 1 increase the diversity among trees                              |
| gamma            | Minimum improvement required for a split | A larger value leads to simpler trees                                      |
| reg_alpha        | L1 regularization                      | Imposes a heavier penalty on less important features                       |
| reg_lambda       | L2 regularization                      | Controls weights and enhances model stability                              |