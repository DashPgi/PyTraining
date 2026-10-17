# Hyperparameter tuning
Hyperparameters are values ​​that you set before training—the model does not learn them from the data itself; tuning them involves searching for a combination that yields the lowest error or the best evaluation metric on unseen data

### Parameter Vs Hyperparameter

| Concept        | Who determines it? | Example                                                      |
| -------------- | ----------------------------- | ------------------------------------------------------------ |
| Parameter      | The model learns it during training | Weights in Logistic Regression, split points in a Decision Tree |
| Hyperparameter | You choose it before training | n_estimators, max_depth, learning_rate, C, gamma               |


# Why Tuning is important?
- Preventing Overfitting
- Preventing Underfitting
- Improving Generalization
    - **The goal** : better score on the validation/test set, not just on the training set!
#### Golden Tip :
Tuning is not a good replace for preprocessing or feature engineering!!
If we haven't good data or have data leak ,also the bestest tuning cant save our model !


## Cross-Validation: The Heart of Tuning
If you perform a single Train/Validation split, the result might depend on that specific data partition. In K-Fold Cross-Validation, the training data is divided into $K$ segments; in each iteration, one segment serves as the validation set while the others are used for training. Finally, the average of the $K$ scores is reported 

- High mean = good performance

- Low standard deviation = consistent performance

- If the mean is good but the test performance is poor, you likely have overfitting or data leakage


## Grid Search
**GridSearchCV** tests all specified combinations. If you have 3 values ​​for **C** and 3 values ​​for **gamma**, it will build exactly 3 × 3 = 9 models. This method is thorough and straightforward, but it becomes computationally expensive very quickly as the number of hyperparameters increases.

## Random Search
In **RandomizedSearchCV**, instead of testing every possible combination, we perform random sampling from specified ranges or distributions. It typically identifies high-quality combinations using a smaller number of trials—especially when only a few hyperparameters are truly significant.