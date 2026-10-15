# Naive-Bayes
A Supervised learning algorithm , It employs Bayes' Theorem to calculate the probability of a sample belonging to each class and ultimately selects the class with the highest probability


It is called "naive" because this algorithm assumes that all features are independent of one another—meaning that a change in one feature does not affect another. *While this assumption does not always hold true in the real world, it works very well in practice*

# Bayes’ Theorem
This concept tells us how to update the probability of an event in light of new evidence


$Formula$ :
$$
P(A\mid B)=\frac{P(B\mid A)\cdot P(A)}{P(B)}
$$

$P(A∣B)$: **Posterior probability** : the probability of A given B (what we want to calculate)

$P(B∣A)$: **Likelihood** : the probability of observing B if A is true

$P(A)$:**Prior probability** : the initial probability of A (before observing)

$P(B)$: **Evidence** : the total probability of B (typically acts as a normalizer)