# Decision-tree
Is a Non-parametric and supervised way with simple conditional rules, It predicts the target value

**A decision tree is like a decision-making diagram consisting of a series of consecutive questions**
## Main parts of a tree
### Root Node
**The important part !!**

The first node of the tree and entire dataset originates from it
### Internal Node
The middle node of the tree that can set another condition on datasets
### Branch
Another part of tree that represents the result of a condition

ForExample in binary we have :
- yes
- no
### Leaf Node
The last node of the tree that show us final prediction 
### Depth
The number of tree levels is from the root to the deepest leaf
## How does DT learn? 
1. All data is placed at the root

2. The model examines all possible features and thresholds

3. It selects the best split

4. The data is divided into two or more segments.

5. The same process is repeated for each segment.

6. Tree growth stops when a stopping condition is met.

## Impurity
The most important concept in a decision tree is impurity