# NumPy: Numerical Computing & Vectorized Mathematics

A comprehensive repository exploring high-performance numerical computing with **NumPy (Numerical Python)**, covering multi-dimensional arrays, vectorization, broadcasting, linear algebra, memory efficiency benchmarks, and applied data analytics mini-projects.

---

## 📌 Overview

NumPy is the foundational library powering nearly all scientific computing and machine learning in Python:
- **N-Dimensional Arrays (`ndarray`):** Vector, matrix, and 3D tensor manipulation.
- **Vectorization vs. Iteration:** Eliminating slow Python `for` loops with optimized C-level vectorized operations.
- **Broadcasting Rules:** Performing arithmetic across arrays of differing compatible shapes.
- **Mathematical & Statistical Operations:** Aggregations across custom axes, linear algebra, logarithms, exponentials, and normalization.
- **Memory & Performance Profiling:** Quantitative benchmarking of Python `list` vs. NumPy `ndarray` memory footprint and execution latency.
- **Mini-Projects:** Real-world applications including student grade normalization, multi-store retail analytics, and sensor outlier filtering.

---

## 📁 Files & Module Breakdown

| File | Type | Description |
|---|---|---|
| [`Basic_NumPy.py`](Basic_NumPy.py) | Python Script | Quick-start reference script demonstrating array instantiation, reshaping, random number generation, aggregations, and broadcasting. |
| [`Numpy_and_modules.ipynb`](Numpy_and_modules.ipynb) | Jupyter Notebook | In-depth masterclass notebook covering array properties (`shape`, `ndim`, `dtype`), indexing/slicing, special matrices (`eye`, `zeros`, `ones`, `linspace`), axis-level aggregations, vector normalization, and execution speed/memory benchmarks. |
| [`Small_Projects.ipynb`](Small_Projects.ipynb) | Jupyter Notebook | Practical project lab containing applied scenarios: student grade analysis, retail store sales calculations, multi-day sensor temperature normalization, and boolean mask filtering. |

---

## 🛠️ Prerequisites & Installation

Install NumPy and Jupyter:

```bash
pip install numpy jupyter
```

---

## 🚀 How to Run

### Run the Quickstart Script
```bash
python Numpy/Basic_NumPy.py
```

### Run the Interactive Notebooks
```bash
jupyter notebook Numpy/
```
- Open [`Numpy_and_modules.ipynb`](Numpy_and_modules.ipynb) for the complete API and mechanics deep dive.
- Open [`Small_Projects.ipynb`](Small_Projects.ipynb) to explore practical problem-solving tasks.

---

## 💡 Key Computational Concepts

### 1. Vectorization & Broadcasting
Vectorized operations execute in compiled C routines, yielding up to $50\times - 100\times$ speedups over standard Python iterations:
```python
import numpy as np

# Broadcasting scalar addition across a 2D matrix
matrix = np.ones((3, 3))
result = matrix + 10  # Evaluates instantly without nested loops
```

### 2. Feature Normalization (Z-Score Standardization)
$$z = \frac{x - \mu}{\sigma}$$
```python
# Standardizing feature vectors for ML models
features = np.array([10.0, 25.0, 32.0, 48.0, 50.0])
standardized = (features - np.mean(features)) / np.std(features)
```

### 3. Boolean Masking & Outlier Filtering
```python
# Filter anomalous readings exceeding thresholds
sensor_data = np.array([21.2, 22.0, 85.6, 21.8, 19.4])
clean_readings = sensor_data[sensor_data < 50.0]
```
