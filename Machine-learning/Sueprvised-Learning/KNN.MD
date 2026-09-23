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