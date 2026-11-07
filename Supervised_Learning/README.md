# Supervised Machine Learning: Foundations, Algorithms & Scratch Implementations

A comprehensive repository of **Supervised Machine Learning** algorithms, spanning regression models, classifiers, ensemble learning methods, mathematical derivations implemented from scratch with NumPy, and applied prediction projects.

---

## 📌 Overview

Supervised learning maps input features $X$ to labeled target outputs $y$:
- **Regression Analysis:** Ordinary Least Squares (OLS), Gradient Descent Linear Regression, Lasso ($L_1$), Ridge ($L_2$), and Support Vector Regression (SVR).
- **Classification Systems:** Logistic Regression, K-Nearest Neighbors (KNN), Gaussian Naive Bayes, Decision Trees, and Support Vector Classifiers (SVC).
- **Ensemble Architectures:** Bagging (Random Forest), Boosting (AdaBoost, Gradient Boosting, XGBoost), Stacking, and Voting classifiers.
- **Implementations from Scratch:** Pure NumPy implementations of KNN, Logistic Regression, and Linear Regression exposing the underlying vector mathematics.
- **Applied Case Studies:** Real estate house price forecasting, employee turnover attrition modeling, health insurance cost estimation, and floral species classification.

---

## 📁 Repository Directory & Component Index

### 1. Algorithms & Models

| File | Paradigm | Algorithm / Topic | Description |
|---|---|---|---|
| [`Linear_Regression.ipynb`](Linear_Regression.ipynb) / [`Linear_Regression_1.ipynb`](Linear_Regression_1.ipynb) | Regression | Linear Regression | Closed-form OLS and gradient-descent line fitting using Scikit-Learn. |
| [`Linear_Regression_scratch.ipynb`](Linear_Regression_scratch.ipynb) | Regression | Linear Regression (Scratch) | Step-by-step vector matrix math computing slope $m$ and intercept $c$ without external ML libraries. |
| [`LROLS.ipynb`](LROLS.ipynb) | Regression | Ordinary Least Squares | Analytical normal equation solution $(\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$. |
| [`Regularization.ipynb`](Regularization.ipynb) | Regression | Lasso & Ridge | Controlling model complexity and multicollinearity via $L_1$ and $L_2$ penalties. |
| [`SVM_regression.ipynb`](SVM_regression.ipynb) | Regression | Support Vector Regression | $\epsilon$-insensitive loss tube fitting with linear and RBF kernels. |
| [`LogisticRegressionScratch.py`](LogisticRegressionScratch.py) | Classification | Logistic Regression (Scratch) | Binary classification using sigmoid activations, log loss, and gradient updates. |
| [`KNN.ipynb`](KNN.ipynb) | Classification | K-Nearest Neighbors | Distance metrics, choosing optimal $k$, and decision boundary visualization. |
| [`KNN_Scratch.py`](KNN_Scratch.py) | Classification | KNN Classifier (Scratch) | Object-oriented NumPy implementation with Euclidean distance and majority voting. |
| [`Naive_bayes.ipynb`](Naive_bayes.ipynb) | Classification | Gaussian Naive Bayes | Probabilistic classification applying Bayes' Theorem with conditional independence. |
| [`Decision_Tree.ipynb`](Decision_Tree.ipynb) | Classification | Decision Trees | Recursive binary splitting using Gini Impurity and Information Gain / Entropy. |
| [`SVM_Classifier.ipynb`](SVM_Classifier.ipynb) | Classification | Support Vector Classifier | Maximal margin hyperplanes and non-linear kernel transformations. |
| [`Random_Forest.ipynb`](Random_Forest.ipynb) | Ensemble | Random Forest | Bootstrap aggregating (Bagging) and random feature subspace sampling. |
| [`AdaBoost.ipynb`](AdaBoost.ipynb) | Ensemble | AdaBoost | Sequential weak learner boosting with dynamic sample weight adjustment. |
| [`Gradient_boosting.ipynb`](Gradient_boosting.ipynb) | Ensemble | Gradient Boosting | Sequential residual error minimization via gradient descent in function space. |
| [`XGBoost.ipynb`](XGBoost.ipynb) | Ensemble | XGBoost | Scalable, regularized gradient boosted decision tree framework. |
| [`Ensemble_Heterogenous.ipynb`](Ensemble_Heterogenous.ipynb) | Ensemble | Voting & Stacking | Blending diverse heterogeneous estimators with a meta-classifier. |

### 2. Applied Prediction Projects & Datasets

| Project / Notebook | Associated Dataset | Problem Statement |
|---|---|---|
| [`House_Price_prediction.ipynb`](House_Price_prediction.ipynb)<br>[`house_price_predictor.ipynb`](house_price_predictor.ipynb) | [`HousePricePrediction.csv`](HousePricePrediction.csv) | End-to-end regression predicting residential real estate transaction prices. |
| [`employee.ipynb`](employee.ipynb) | [`employee_turnover.csv`](employee_turnover.csv) | Predicting staff attrition and turnover probability using regularized classification. |
| [`iris_Flower.ipynb`](iris_Flower.ipynb) | [`Iris.csv`](Iris.csv) | Multi-class floral species benchmark evaluating KNN and Decision Trees. |
| Exploration Resource | [`insurance.csv`](insurance.csv) | Healthcare insurance claims dataset for regression modeling. |

---

## 🛠️ Prerequisites & Installation

Install the machine learning stack:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn xgboost jupyter
```

---

## 🚀 How to Run

### 1. Test from Scratch Implementations
Run the pure NumPy algorithmic scripts directly:
```bash
# Test K-Nearest Neighbors from scratch
python Supervised_Learning/KNN_Scratch.py

# Test Logistic Regression gradient descent from scratch
python Supervised_Learning/LogisticRegressionScratch.py
```

### 2. Launch Interactive Modeling Notebooks
```bash
jupyter notebook Supervised_Learning/
```
- Open [`Decision_Tree.ipynb`](Decision_Tree.ipynb) for tree pruning and structure visualization.
- Open [`XGBoost.ipynb`](XGBoost.ipynb) for state-of-the-art gradient boosted trees.
- Open [`House_Price_prediction.ipynb`](House_Price_prediction.ipynb) for the complete housing regression pipeline.

---

## 💡 Algorithmic Mathematical Highlights

### Logistic Regression Sigmoid & Gradient Update
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$
$$\frac{\partial J}{\partial \mathbf{w}} = \frac{1}{m} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y})$$

### Ridge vs. Lasso Penalty Formulation
$$\mathcal{L}_{\text{Ridge}} = \text{MSE} + \lambda \sum_{j=1}^p w_j^2 \quad \text{vs.} \quad \mathcal{L}_{\text{Lasso}} = \text{MSE} + \lambda \sum_{j=1}^p |w_j|$$
