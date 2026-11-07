# Practice Codes & Machine Learning Algorithms Lab

A comprehensive repository of algorithmic implementations, metaheuristic optimization techniques, machine learning practical labs, hyperparameter tuning experiments, and core programming problem sets.

---

## 📌 Overview

This laboratory contains code spanning mathematical optimization, classical statistical machine learning, university practical experiments, and foundational data structures:
- **Mathematical Optimization & Metaheuristics:** Implementations of Gradient Descent, Momentum, RMSProp, Genetic Algorithms (GA), Particle Swarm Optimization (PSO), and Grey Wolf Optimization (GWO).
- **Support Vector Machines (SVM):** Hard-margin, soft-margin slack formulations, and non-linear kernel transformations.
- **Model Evaluation & Hyperparameter Search:** Exhaustive Grid Search (`GridSearchCV`), Randomized Search (`RandomizedSearchCV`), bias-variance tradeoff diagnostics, and Mean Squared Error (MSE) loss metrics.
- **Curriculum Practical Series:** Academic lab notebooks (`practical-1` to `practical-8`) covering end-to-end data pipelines, regression, classification, and diagnostics.
- **Foundational Coding Drills:** Targeted practice notebooks for Python OOP, data structures, NumPy arrays, and Pandas DataFrames.

---

## 📁 Repository Structure & Taxonomy

### 1. Optimization & Metaheuristic Algorithms

| File | Category | Description |
|---|---|---|
| [`Gradient_decent.py`](Gradient_decent.py) / [`Gradient_desent.py`](Gradient_desent.py) | Gradient-Based | First-order iterative optimization computing parameter gradients with respect to loss functions. |
| [`Momentum + RMSProp.ipynb`](<Momentum + RMSProp.ipynb>) / [`RMSProp.py`](RMSProp.py) | Advanced Optimizers | Adaptive learning rate optimization using exponential moving averages of squared gradients to dampen oscillations. |
| [`Convex_&_Non_convex_Function.py`](Convex_&_Non_convex_Function.py) | Mathematical Analysis | Analyzing convergence properties across global minima (convex) versus saddle points and local minima (non-convex). |
| [`Genetic_algo.py`](Genetic_algo.py) / [`GA_Parameter.py`](GA_Parameter.py) | Evolutionary Algorithm | Simulates natural selection: chromosome population initialization, fitness scoring, crossover mating, and mutation. |
| [`Partical_swarn_optimizartion.py`](Partical_swarn_optimizartion.py) | Swarm Intelligence | Simulates flocking behavior where candidate particles adjust trajectories based on personal best and global swarm best. |
| [`GWO.py`](GWO.py) | Nature-Inspired | Grey Wolf Optimizer tracking alpha, beta, delta leadership hierarchy to encapsulate prey in multi-dimensional search spaces. |
| [`Hybrid_optimization.py`](Hybrid_optimization.py) | Hybrid Search | Blending global exploration (metaheuristics) with local exploitation (gradient descent) for resilient convergence. |
| [`Primal_optimization.py`](Primal_optimization.py) | Constrained Optimization | Formulating primal optimization problems and evaluating Karush-Kuhn-Tucker (KKT) conditions. |

### 2. Machine Learning Mechanics & Support Vector Machines

| File | Focus | Description |
|---|---|---|
| [`Hard_margin.py`](Hard_margin.py) | Linear SVM | Exact hyperplane separation without misclassifications for linearly separable training data. |
| [`Soft_margin.py`](Soft_margin.py) | Regularized SVM | Soft-margin optimization with penalty constant $C$ and slack variables ($\xi$) to balance margin width and margin violations. |
| [`Kernal_trick.py`](Kernal_trick.py) | Kernel Methods | Implicitly mapping non-linearly separable points into higher-dimensional feature spaces via kernel functions. |
| [`FEature_selection.py`](FEature_selection.py) | Feature Engineering | Evaluating feature importance scores to prune redundant or noisy inputs. |
| [`Model_fitting_check.py`](Model_fitting_check.py) | Diagnostics | Empirical analysis of model fitting: identifying underfitting (high bias) vs overfitting (high variance). |
| [`Model_complexity_comparison.py`](Model_complexity_comparison.py) | Comparative Study | Comparing performance across simple linear models vs complex non-linear estimators. |
| [`MSE.py`](MSE.py) | Loss Metrics | Step-by-step computation of Mean Squared Error loss functions and their gradients. |
| [`Geometric_interpretation.py`](Geometric_interpretation.py) | Geometry of ML | Visualizing hyperplanes, normal vectors, and Euclidean distances to decision boundaries. |

### 3. Hyperparameter Tuning & Model Selection

| File | Method | Description |
|---|---|---|
| [`Grid_search.py`](Grid_search.py) | Exhaustive Grid Search | Systematic cross-validated hyperparameter tuning evaluating the Cartesian product of hyperparameter grids using Scikit-Learn. |
| [`RandomSearchCV.py`](RandomSearchCV.py) | Randomized Search | Stochastic sampling from parameter distributions to identify optimal hyperparameter sets faster than brute-force grids. |
| [`Search.py`](Search.py) / [`Search_technique.py`](Search_technique.py) | Search Algorithms | Algorithmic state-space search routines. |

### 4. Practical Coursework Series

Progressive lab notebooks implementing applied machine learning:
- [`practical-1.ipynb`](practical-1.ipynb): Data ingestion, exploratory inspection, feature scaling, and data normalization.
- [`Practical-2.ipynb`](Practical-2.ipynb): Vector projections, inner products, $L_1$, $L_2$, and $L_\infty$ norms.
- [`practical-3.ipynb`](practical-3.ipynb) / [`practical3.ipynb`](practical3.ipynb): Linear regression models and cost curve plotting.
- [`practical-4.ipynb`](practical-4.ipynb) / [`practical4.ipynb`](practical4.ipynb): Logistic regression, decision boundaries, and binary classification metrics.
- [`practical_5.ipynb`](practical_5.ipynb) / [`practical5.ipynb`](practical5.ipynb): Multi-class classification and confusion matrix visualization.
- [`practical-7 (1).ipynb`](<practical-7 (1).ipynb>): Ensemble methods, Decision Trees, and Random Forests.
- [`practical-8 (2).ipynb`](<practical-8 (2).ipynb>): Unsupervised clustering (K-Means, Hierarchical) and dimensionality reduction (PCA).

### 5. Modular Practice Subdirectories

- **[`python/`](python/)**: 12 dedicated Jupyter notebooks testing core Python syntax:
  - Data Types & Control: [`if-else.ipynb`](python/if-else.ipynb), [`Loops.ipynb`](python/Loops.ipynb), [`operator.ipynb`](python/operator.ipynb), [`type_conversion.ipynb`](python/type_conversion.ipynb).
  - Data Structures: [`List.ipynb`](python/List.ipynb), [`Tuple.ipynb`](python/Tuple.ipynb), [`Set.ipynb`](python/Set.ipynb), [`Dictionary.ipynb`](python/Dictionary.ipynb).
  - Modularity: [`Function.ipynb`](python/Function.ipynb), [`Classes.ipynb`](python/Classes.ipynb) (OOP principles).
- **[`Numpy/`](Numpy/)**: Fast-paced array drills in [`Creating_array_from_list.ipynb`](Numpy/Creating_array_from_list.ipynb).
- **[`Pandas/`](Pandas/)**: DataFrame querying in [`filtering_data_using_query.ipynb`](Pandas/filtering_data_using_query.ipynb), [`selecting_data.ipynb`](Pandas/selecting_data.ipynb), [`Methods_df.ipynb`](Pandas/Methods_df.ipynb), and production model persistence with [`sentinel_model.pkl`](Pandas/Data%20cleaning/sentinel_model.pkl).

---

## 🛠️ Prerequisites & Installation

```bash
pip install numpy pandas scipy scikit-learn matplotlib jupyter joblib
```

---

## 🚀 Running the Experiments

Execute any algorithm script directly:

```bash
# Test Particle Swarm Optimization
python Practice-Codes/Partical_swarn_optimizartion.py

# Test Grey Wolf Optimizer
python Practice-Codes/GWO.py

# Run Hyperparameter Grid Search
python Practice-Codes/Grid_search.py
```

Or explore the coursework notebooks in Jupyter:
```bash
jupyter notebook Practice-Codes/
```
