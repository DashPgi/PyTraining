# KNN
### K-Nearest Neighbors
**A supervised machine learning algorithm for classification and regression too**

this algorithm check nearest data of our selected data and Based on neighbor data, guess our data

## How Does it work?
### Select K values
K value of our neighbor's data
### Distance calculation
We calculate the distance between the new data point and all the training data points
### Find K nearest neighbor of data
We sort the data based on distance and select the K nearest ones
### Voting
1.  **Classification** : Among these K neighbors, we observe which category (class) appears most frequently. We then assign the new data point to that category 
2. **Regression** : We calculate the average of the K-neighbor values ​​and use it as the prediction


## Distance Metrics
for that how we can find nearest neighbor of data we should define distance :
### 1. Euclidean Distance
$$
d(x,y) = \sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
$$
### 2. Manhattan Distance
$$
d(x,y) = \sum_{i=1}^{n} |x_i-y_i|
$$
### 3. Minkowski Distance
$$
d(x,y) =
\left(
\sum_{i=1}^{n} |x_i-y_i|^p
\right)^{1/p}
$$
**if p = 1 => Euclidean**

**if p = 2 => Manhattan**
### 4. Hamming Distance
It is used for categorical or binary data. It counts the number of positions where two vectors differ

---
| K Value               | Effect                                                                                        |
| --------------------- | --------------------------------------------------------------------------------------------- |
| Very small K (e.g., 1) | The model becomes overly sensitive to the training data (Overfitting). It learns noise as well. |
| Very large K          | The model becomes too simple (Underfitting). It fails to learn decision boundaries effectively. |
| Balanced K            | Strikes a good balance between bias and variance. |
## How find best K value?
1. Cross-Validation: The best approach. You test various values ​​of K and select the one that yields the lowest error on the test data

2. Choose an odd number: For classification, it is best to use an odd K to avoid a tie in the voting

3. Rule of thumb: Setting K ≈ √n (where n is the number of training samples) is usually a good starting point

## With python
```
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train_scaled, y_train)

predictions = knn.predict(X_test_scaled)

accuracy = knn.score(X_test_scaled, y_test)
print(f"Accuracy: {accuracy:.2f}")
```