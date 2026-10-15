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


$In-Classification : $

$$
P(y\mid X)=\frac{P(X\mid y)\cdot P(y)}{P(X)}
$$

**We select the class that has the highest** $P(y|X)$



## Why Naive?
In the real world, features are often dependent. For example, in an email, the words "winner" and "prize" usually appear together. However, Naive Bayes assumes:    
$$
P(X\mid y)=P(x_1\mid y)\cdot P(x_2\mid y)\cdot \ldots \cdot P(x_n\mid y)
$$

This means the probability of the set of all features is equal to the product of the probabilities of the individual features *(cause we assume they are independent)*

## Type Of Naive Bayes

| Type                    | Application                        | Distribution Assumption | Example                            |
| ----------------------- | ---------------------------------- | ----------------------- | ---------------------------------- |
| Gaussian Naive Bayes    | Continuous data (e.g., height, weight, temperature) | Normal (Gaussian) distribution | Predicting disease based on numerical symptoms |
| Multinomial Naive Bayes | Discrete data (e.g., word counts)  | Multinomial distribution | Text classification, sentiment analysis |
| Bernoulli Naive Bayes   | Binary data (0 or 1)               | Bernoulli distribution  | Presence or absence of a word in a text |