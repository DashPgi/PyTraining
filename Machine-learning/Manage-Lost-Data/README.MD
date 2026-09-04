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
