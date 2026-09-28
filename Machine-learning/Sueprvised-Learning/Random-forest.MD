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

# Advantage of Random Forest 
| Advantage | Explanation
| ------------------------- | ------------------------------------------------------------ |
| High accuracy |Usually more accurate than a single Decision Tree |
| Resistant to Overfitting | because it uses the average of several trees|
| Working with big data |Works well with large and high-dimensional data |
| The importance of features |It can show the importance of each feature in the prediction  |
| Little need for preprocessing| It is not sensitive to data normalization or scaling
| Outlier resistant |Outliers have little effect on the final  
# Disadvantages of Random Forest
| Drawback             | Explanation                                                                      |
| -------------------- | -------------------------------------------------------------------------------- |
| Prediction speed     | With hundreds of trees, prediction is slower than with a simple model            |
| Interpretability     | Not as interpretable as a simple decision tree (relatively a "black box")        |
| Memory               | Results in a larger model compared to simpler algorithms                         |
| Text/Image data      | Not as powerful as Deep Learning for raw data like text or images                |

## Important Parametics
| Parameter         | Description                        | Suggested Value               |
| ----------------- | ---------------------------------- | ----------------------------- |
| n_estimators      | Number of trees in the forest      | 100–500                       |
| max_depth         | Maximum depth of each tree         | None or 10–20                 |
| min_samples_split | Minimum samples to split a node    | 2–10                          |
| min_samples_leaf  | Minimum samples in leaf nodes      | 1–5                           |
| max_features      | Number of random features per split| √p (classification), p/3 (regression) |
| bootstrap         | Whether to use bootstrapping       | True                          |

# With Python 
```
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# ساخت مدل Random Forest
rf = RandomForestClassifier(
    n_estimators=100,  
    max_depth=10,      
    random_state=42       
)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

importances = rf.feature_importances_
```