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