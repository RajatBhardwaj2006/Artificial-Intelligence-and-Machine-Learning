# Pandas: Data Wrangling, Cleaning & Exploratory Analysis

A comprehensive repository dedicated to **Pandas**, the industry-standard Python library for data manipulation, cleaning, aggregation, exploratory data analysis (EDA), and tabular data operations.

---

## 📌 Overview

Mastering Pandas is essential for transforming noisy, raw datasets into clean features for machine learning pipelines:
- **Core Structures:** `Series` (1D labeled arrays) and `DataFrame` (2D labeled tables).
- **Indexing & Slicing:** Label-based selection with `.loc[]` vs. integer-position selection with `.iloc[]`.
- **Data Ingestion:** Reading from and writing to multiple file formats (CSV, JSON).
- **Data Cleaning:** Detecting and handling missing data (`isna()`, `dropna()`, `fillna()`), removing duplicates, and casting data types.
- **Real-World Analytics:** Analyzing real-world datasets including a massive global air quality environmental dataset (`globalAirQuality.csv`) and employee HR records.
- **Assignments & Exercises:** Complete question-and-answer notebooks reinforcing practical data science problem solving.

---

## 📁 Files & Notebooks Breakdown

### 1. Notebooks & Python Scripts

| File | Type | Description |
|---|---|---|
| [`Pandas_and_Modules.ipynb`](Pandas_and_Modules.ipynb) | Jupyter Notebook | Complete fundamentals guide: Series creation, DataFrame construction, schema inspection (`info()`, `describe()`), and basic slicing. |
| [`Working_on_data.ipynb`](Working_on_data.ipynb) | Jupyter Notebook | Large-scale analysis on the `globalAirQuality.csv` dataset, demonstrating `.loc`, `.iloc`, conditional boolean filtering, grouping, and aggregations. |
| [`Data_cleaning.ipynb`](Data_cleaning.ipynb) | Jupyter Notebook | End-to-end data cleansing workflows: imputation techniques, deduplication, handling outliers, and string cleaning. |
| [`Assignment_Problems_solve.ipynb`](Assignment_Problems_solve.ipynb) | Jupyter Notebook | Solved assignments covering data analysis on the Iris dataset, statistical summaries, percentiles, and multi-condition queries. |
| [`Practice_Problems.ipynb`](Practice_Problems.ipynb) | Jupyter Notebook | Hands-on challenge problems focusing on DataFrame manipulations, sorting, and computed column assignments. |
| [`Compute_mean.py`](Compute_mean.py) | Python Script | Minimal starter script demonstrating DataFrame instantiation and column-wise mean computation. |

### 2. Datasets Included

| Dataset File | Format | Description |
|---|---|---|
| [`globalAirQuality.csv`](globalAirQuality.csv) | CSV (~2 MB) | Global environmental dataset recording air quality metrics, pollutants, and measurement stations worldwide. |
| [`employee_data (2).csv`](<employee_data (2).csv>) | CSV | Tabular corporate dataset with employee details, departments, and salaries. |
| [`employees.json`](employees.json) | JSON | Semi-structured JSON records for practicing schema flattening and JSON ingestion. |
| [`raw_data (1).csv`](<raw_data (1).csv>) | CSV | Raw uncleaned data containing missing values and inconsistent formatting. |
| [`Sorted_data.csv`](Sorted_data.csv) | CSV | Output dataset demonstrating post-sorting and filtering transformations. |

---

## 🛠️ Prerequisites & Installation

Install Pandas and Jupyter:

```bash
pip install pandas numpy jupyter
```

---

## 🚀 How to Run

### Run the Quick Test Script
```bash
python Pandas/Compute_mean.py
```

### Launch the Notebooks
```bash
jupyter notebook Pandas/
```
- Open [`Pandas_and_Modules.ipynb`](Pandas_and_Modules.ipynb) for core mechanics.
- Open [`Working_on_data.ipynb`](Working_on_data.ipynb) to inspect the global air quality analysis.
- Open [`Data_cleaning.ipynb`](Data_cleaning.ipynb) for null-handling pipelines.

---

## 💡 Essential Pandas Patterns Demonstrated

### 1. Label vs. Positional Indexing
```python
# Label-based (.loc)
df.loc[df['city'] == 'Delhi', ['pollutant', 'value']]

# Integer-position based (.iloc)
df.iloc[0:5, 1:4]
```

### 2. Missing Value Imputation
```python
# Check for nulls
df.isna().sum()

# Impute numeric columns with median to resist outliers
df['salary'] = df['salary'].fillna(df['salary'].median())
```

### 3. Grouped Aggregations
```python
# Calculate mean and max value by country/pollutant
df.groupby(['country', 'pollutant'])['value'].agg(['mean', 'max', 'count'])
```
