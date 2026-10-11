# Manage Lost Data

## Type of Missing Data
1. MCAR -> Missing Completely at Random
    - The data is missing **completely at random** and has no relationship with the other variables.

2. MAR -> Missing at Random
    - The data is **not missing at random**, but we can predict the missing values using other variables.

3. MNAR -> Missin not at Random
    - The missing data **depends on the missing values themselves**, and we do not have any auxiliary variables to help predict them.

## Methods for identifying

- Counts and percentages
- Pattern identification
- MCAR test

## How To Manage

### Deleting Datas

- Rows Deleting <code>when < 5%</code>
- Columns Deleting <code>when > 50%</code>

### Simple Imputations
- Mean <code>For data that have less outliers and close together</code>
- Median <code>For data that have more outliers and far 
</code>
- Mode <code>For Categories</code>
- Constants
- Backward fill / Forward Fill

### Advance Imputations

- KNN
- MICE
- ML models

### Deep learning

- Masking + Embedding
- Marginalization over Missing Values

---
| Missing Percentage | Missingness Type | Data Type   | Recommended Method                        |
| ------------------ | ---------------- | ----------- | ----------------------------------------- |
| < 5%               | MCAR             | Any type    | Row deletion or Mean/Median imputation    |
| 5–20%              | MAR              | Numerical   | KNN or Iterative Imputer                  |
| > 20%              | MAR              | Numerical   | MICE or ML-based methods                  |
| Any percentage     | MNAR             | Any type    | Missingness Indicator + specialized model |
| Time Series        | MAR/MNAR         | Numerical   | Forward/Backward Fill or GRU-D            |
| Categorical Data   | MAR              | Categorical | Mode or KNN with Encoding                 |

### Deep Learning

Neural networks can be used for complex missing-data problems, especially with large datasets.

Examples:

- Autoencoders
- RNNs
- GRUs
- Transformers

---

## 6. Missingness Indicator

Sometimes the fact that a value is missing is itself informative.

A Missingness Indicator is an additional feature that records whether the original value was missing.

For example:

**0 → Value was present**

**1 → Value was missing**

This can be particularly useful when the reason for missingness contains predictive information.

---

## 7. Group-Wise Imputation

Instead of using one statistic for the entire dataset, missing values can be imputed separately within meaningful groups.

For example, missing salary values could be filled using the median salary of the corresponding department rather than the median salary of the entire dataset.

This approach can preserve important differences between groups.

---

## 8. Time-Series Missing Data

For time-series data, the temporal order must be considered when handling missing values.

Common approaches include:

- Forward Fill
- Backward Fill
- Interpolation
- Kalman Filtering
- Time-aware Machine Learning models
- GRU-D

The appropriate method depends on the nature of the time series and the reason for the missing values.

---

## 9. Data Leakage

Imputation must be performed carefully to avoid **Data Leakage**.

Imputation statistics or models should be learned using the training data only and then applied to validation and test data.

Using information from the test set during imputation can cause overly optimistic model performance.

A proper Machine Learning pipeline should separate the fitting of the imputation method from its application to unseen data.
