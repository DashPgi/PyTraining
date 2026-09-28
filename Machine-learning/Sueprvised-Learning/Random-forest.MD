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
### 2. Crea