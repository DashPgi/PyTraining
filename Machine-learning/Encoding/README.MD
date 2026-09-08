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