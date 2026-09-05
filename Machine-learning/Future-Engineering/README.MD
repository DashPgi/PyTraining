# feature Engineering

## What is FE?

Feature engineering is the process of using domain knowledge to extract or construct new variables (features) from raw data so that machine learning models can better learn patterns and increase prediction accuracy.

## Why we Should using Fe ?

- Better FE -> Better Signal For Learning -> Better Accuracy
- No FE -> No good Accurancy
- set up and convert non-numerical data to numerical for better learning (cause Machine's Languge is numerical but data is dirty,imperfect and raw)
- If FE does't exist, even the powerfull algorithm will fail
- without FE -> More Problem -> More Bugs and less Accuracy

## feature Engineering Cycle

1. Understanding the Problem
2. Data Collecting
3. Clearing Data
3. Exploration analysis
    - Discovering patterns, correlations, distributions.
5. Fe
    - Build
    - Transform 
6. Select features
7. Test on Models
    - Choosinga best model for understanding new features
8. Supervision

## Techniques

- Manage Data
    - Delete
    - Imputation
    - Pointer

- Encoding Data
    - One-hot Encoding : for nominal datas
    - Label Encoding : for ordered datas
    - Target Encoding : for  Replacing each category with the mean of the target variable for that category

- Numerical Transformation 
    - Scalling : Standard & min/max & Robust
    - Binning
    - Log Transform

- Manage Outliers
    - Remove
    - Scapping
    - Convert with Log or Sqrt

- Datetime Features

- Feature Construction
    - using domain knowledge for mixing or Derivative data to create new features

- Text Features
    - Text length
    - Number of keywords
    - Presence of special characters 
    - TF-IDF or Word Embeddings: To convert text into a numeric vector.

- Time-Series Features 
    - Lag
    - Rolling windows
    - Season features

## Feature Selection
**Goal: Preserve useful features and remove noise to prevent overfitting and reduce computational cost.**
- Use Variance
- Deleting data with high Solidarity
- Use Selectkbeast
- Importance of features from models
- RFE `Recursive Feature Elimination`

## Dimensionality Reduction
**PCA** ``Principal Component Analysis``:
Converting correlated features into independent principal components.

**UMAP / t-SNE** :
for visualization, not modeling.

**Autoencoder** : 
Deep learning for feature compression.


- Monitoring in production