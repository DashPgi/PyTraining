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