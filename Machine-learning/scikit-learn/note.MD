# Scikit Learn

## Ml Concept
We have three type of machine learning :
#### 1. Supervised
Datas have label 
#### 2. Unsupervised
Datas haven't label and model classification itself
#### 3. Reinforcement
In this type model learn with rewards and punishments

--- 
### also we have two type of output from models :

- Classifications 
  - Outputs are class
- Regression 
  - Output are numeric

---
### Key Words : 

- Feature or X 
- Target or Y
- Sample

## Step By Step
### 1. create a model 
### 2. Train the model
### 3. Make prediction
### 4. Evaluate the model

## Classification
## Regression
a numeric output

Fit the best line through the points

## Pipeline 

 A pipeline combines multiple steps into a single "unified model." It handles the sequential execution of these steps; most importantly, during the `fit` phase, it learns exclusively from the training data, while during the `predict` phase, it only performs transformations

--- 

### Tip 
Use the test data only once, at the very end. All selection and tuning processes—including GridSearch—must be performed exclusively on the training set using cross-validation (CV). If you repeatedly modify your model based on the test results, you have effectively "memorized" the test set, and it no longer provides an honest estimate

## Model Selection