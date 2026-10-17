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