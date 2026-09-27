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

**We must dicrease impurity with decision-tree**
## Gini Impurity
One of the most common metrics for classification is Gini Impurity.

### Formula : 
$$
\text{Gini} = 1 - \sum_{i=1}^{C} p_i^2
$$

$C$ = a number of classes

$iP$ = The proportion of class 𝑖 instances at the node

$for-two-class$ : 
$$
\text{Gini} = 1 - \left(p_1^2 + p_2^2\right)
$$
$if$

$$Gini -Close-to-0 = Puritier$$

$if$

$$Gini-bigger-than-0 = Impuritier$$

## Entropy 
It measures the degree of disorder or uncertainty in a node

### Formula :
$$
\text{Entropy} = -\sum_{i=1}^{C} p_i \log_2(p_i)
$$

$for-two-class$

$$
\text{Entropy} = -\left(p_A\log_2(p_A) + p_B\log_2(p_B)\right)
$$

$if$

$$ Entropy = 0 \rightarrow uncertainty = 0$$

$if$

$$ Entropy > 0 \rightarrow uncertainty > 0$$

## Gini Vs Entropy
| Feature          | Gini                      | Entropy                                    |
| ---------------- | ------------------------- | ------------------------------------------ |
| Metric Type      | Impurity                  | Uncertainty                                |
| Formula          | $1 - \sum p_i^2$          | $-\sum p_i \log_2 p_i$                     |
| Computation Speed| Slightly faster           | Slightly slower                            |
| Zero Value       | Pure node                 | Pure node                                  |
| Usage            | Very common in CART       | Based on Information Gain                  |
| Practical Result | Usually similar to Entropy| Usually similar to Gini                    |

## Information Gain
indicates how much uncertainty a split has reduced

### Formula :
$$
IG = \text{Entropy(parent)} -
\sum_j \frac{N_j}{N}\text{Entropy(child}_j\text{)}
$$
**The higher the Information Gain, the better the split. Information Gain is the difference in entropy before and after the split**