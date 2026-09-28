# Random-forest
A ensemble learning algorithm that which employs a combination of decision trees for more accurate prediction

#### Single Decision Tree Problem
**A decision tree easily overfits** (meaning it memorizes the training data but performs poorly on new data).
#### Solution :
- Instead of a decision tree ,we planting hundreds decision tree
- Each tree is trained on a subset of the data and features
- Ultimately, we aggregate the opinions of all the trees (**voting**)
# How does it works?
### 1. Bootstrap Sampling 
- We draw several random samples with replacement from the original data
- We use all of data randomly for each tree even with repeatition
    - ForExample : we have 1000 dataset ,set 1000 dataset randomly for every smiple or tree
- Some data are selected multiple times, while others are not selected at all
### 2. Create decision trees
- For every bootstrap, we create a decision tree
- At each node of the tree, we allow only a random subset of features to be selected for the split
### 3. Predict or Voting
$For$ **$Classification$** : Each tree predicts a class, and the class that receives the most votes becomes the final output

$For$ **$Regression$** : We calculate the average of the predictions from all the trees