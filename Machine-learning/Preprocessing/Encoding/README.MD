# Encoding

## Type of Categoricals data 

1. **Nominal** : for No ordered datas
2. **Ordinal** : for ordered datas

**Tip** : ``The best choice of encoding method depends on Cardinality``

## Methods

- **One-hot** 
    - for Nominal datas
    - Creates a binary column for each category (1=present, 0=absent)
    - Does not create false order; great for linear models
    - Dimensions explode as the number of categories increases (Sparse)
- **Label**
    - For Ordinal datas
    - Gives each category an integer (0,1,2,…)
    - Only for binary data or tree models
    - Simple and compact
    - Creates pseudo-orders for Nominal data in linear/SVM/KNN models
- **Ordinal**
    - For Ordinal datas
    - Like Label Encoding but with a manually defined order.
    - Ordinal data that has a meaningful order 
    - Preserves the actual order.
    - If the order is defined incorrectly, the model will be misled.
- **Target(Mean)**
    - For High Cardinality datas
    - Replaces each category with the target average of that category.
    - Does not increase dimensions; strong for tree models
    - Risk of data leakage; requires CV and smoothing
- **Frequency**
    - For High Cardinality datas
    - Replaces each category with its number or frequency in the data.
    - best for tree's model
    - No information leakage; simple
    - Does not directly provide information about the relationship with the target
- **Binary/Hash**
    - For High Cardinality datas
    - Maps categories to binary codes or fixed hashes
    - Reduced dimensions compared to OHE
    - Collisions may occur in the hash.

## Tips
### Identify the variable type
Nominal → OHE or Binary/Hash; Ordinal → Ordinal Encoding with explicit ordering; Binary → Label Encoding is safe 

### Measure Cardinality
If the number of categories is large (>15), OHE overestimates the dimensions; in this case, Target Encoding (with caution), Frequency Encoding, or Hashing are better.

### What's model type

Tree models (such as XGBoost, LightGBM) with Label Encoding on Nominal usually have no problem, but linear models, SVM, KNN and neural networks are sensitive to false order and OHE/Target performs better.

### Prevent Dataleakge

Always split the data into train/validation/test before encoding. For Target Encoding, be sure to use cross-validation within the train and never use the entire target data to calculate the average of the clusters.

### Unknown categories at inference time

In production you may see a new category; use handle_unknown in encoders and have a fallback strategy (like "Other" category or overall average).

## Encoding for text, time, and numeric data
- Text
    - Vectorization methods such as Bag-of-Words, TF-IDF, or pre-trained embeddings (such as Word2Vec, FastText, or Transformer models) are used. These transform text into numerical vectors with statistical/semantic meaning.
- Data/Time
    - Extracting cyclic features (hour, day of the week, month) and converting them with cyclic encoding with sine/cosine functions to maintain time continuity (e.g. 23 hours is close to 0 hours).
- Continuous numbers
    - They usually do not require encoding, but scaling (Standardization/MinMax) and sometimes nonlinear transformations (Log, Box-Cox) are useful to improve model convergence.

## Train/Test

**Train/test split means dividing the data into two separate parts before training the model**
- train for learning the parameters and test for honestly evaluating performance on “unseen” data. This prevents the huge error of “false optimism” (apparent overfitting) and gives a true measure of the model’s generalization ability.

### Why Train/test?
- **Generalizability assessment**
    - A model that only performs well on trained data will fail in the real world; the test set is a simulation of future/unknown data.
- **Prevent dataleakage**
    - If test (or future) data infiltrates the train during preprocessing or encoding, the metrics become unrealistic and overly optimistic.
- **Meaningful decisions**
    - The choice between models, hyperparameters, and preprocessing strategies should be based on valid criteria, not the chance of a particular split.

### Big Three
- **Train** : The model learns its parameters here (coefficients, tree nodes, network weights).
- **Validation** : Used to tune hyperparameters, select features, and compare models; multiple touches are allowed.
- **Test** : Used only once, at the end, for the final report; should not be used to make decisions or change the model.

| Data size | Common suggestion | Why |
| --------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| Small (<10K samples) | 60% train / 20% val / 20% test or better: K-Fold CV | Data is sparse; holdout gets noisy, CV is more stable |
| Medium (10K to 1M) | 70–80% train / 10–15% val / 10–15% test | Good balance between training and evaluation |
| Large (>1M) | 98% train / 1% val / 1% test | Even 1% of millions of samples is enough |

## Type of Split 

- **Stratified Split** : In classification with unbalanced classes, the ratio of classes in train/test is maintained to ensure fair evaluation.
- **Temporal Split** : For temporal data, never split randomly; train should be past and test should be future to avoid temporal leakage.
- **Grouped Split** : When multiple rows belong to the same group (a user, a patient, a device), the group should not be in both train and test; otherwise the evaluation will be unrealistic.

## The golden rule to prevent leakage

All preprocessing (including encoding, scaling, imputation) is done only on train fit, then the same transformers are applied (transformed) on val/test. Implement this easily and safely with Pipeline + ColumnTransformer in sklearn.

**Leakage symptoms:**

- Accuracy/"near perfect" metrics on a non-trivial task.

- A feature with an unreasonably high importance (probably containing target or future information).

- The model performs very well on train/test, but poorly in production.

## Best Practices

* **Build a Pipeline** : Put all preprocessing steps (including encoding) in a sklearn Pipeline with ColumnTransformer to apply the same to train and test and avoid leakage.

* **Manage rare classes** : Merge very low frequency classes into an "Other" class or use Target/Frequency Encoding to reduce noise.

* **Use smoothing and K-Fold for Target Encoding** : to avoid overfitting to high-level classes.

* **Use Dummy Variables in linear models** : i.e. remove a column after OHE to avoid multicollinearity.

* **Monitor drift in production** : the distribution of classes may change over time; keep encoders and fallback strategies up to date.

