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
**GridSearchCV** tests all specified combinations. If you have 3 values ​​for **C** and 3 values ​​for **gamma**, it will build exactly 3 × 3 = 9 models. This method is thorough and straightforward, but it becomes computationally expensive very quickly as the number of hyperparameters increases

## Random Search
In **RandomizedSearchCV**, instead of testing every possible combination, we perform random sampling from specified ranges or distributions. It typically identifies high-quality combinations using a smaller number of trials—especially when only a few hyperparameters are truly significant


## Bayesian Optimization
*Grid Search* tries everything indiscriminately, while *Random Search* operates randomly. **Bayesian Optimization**, however, uses the results from previous experiments to estimate which region of the search space is likely to yield better outcomes; consequently, it typically achieves good results with fewer experiments


## Hyperband and Early Stopping
The concept behind Hyperband is as follows: initially allocate a small budget to a large number of configurations, discard the underperforming ones early, and dedicate more resources to the promising candidates. This approach is highly effective for models that are time-consuming to train, such as neural networks


# In another algorithm 
| Model               | Key Hyperparameters                                                             | Primary Effect                         |
| ------------------- | ------------------------------------------------------------------------------- | -------------------------------------- |
| KNN                 | n_neighbors, weights, metric                                                    | Number of neighbors and weighting scheme |
| Decision Tree       | max_depth, min_samples_split, min_samples_leaf, ccp_alpha                       | Controlling complexity and overfitting   |
| Random Forest       | n_estimators, max_depth, max_features, min_samples_leaf                         | Diversity and depth of trees           |
| SVM                 | C, gamma, kernel                                                                | Decision boundary, flexibility, and error penalty |
| Logistic Regression | C, penalty, solver                                                              | Strength of regularization             |
| XGBoost             | n_estimators, learning_rate, max_depth, subsample, colsample_bytree, reg_lambda | Learning rate, complexity, and regularization |