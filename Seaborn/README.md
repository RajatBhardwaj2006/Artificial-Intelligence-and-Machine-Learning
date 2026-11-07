# Statistical Data Visualization with Seaborn

A practical exploration of statistical plotting using **Seaborn**, covering multi-variable relationships, categorical distributions, continuous probability densities, heatmaps, and faceted grid layouts.

---

## 📌 Overview

Seaborn extends Matplotlib by providing an intuitive, declarative API for statistical exploration:
- **Relational Plots:** Mapping dimensions to aesthetics (`x`, `y`, `hue`, `size`, `style`) using `sns.relplot` and `sns.scatterplot`.
- **Categorical Distributions:** Visualizing medians, variance, and spreads across categories using `sns.boxplot`, `sns.violinplot`, and `sns.barplot`.
- **Distribution Estimates:** Kernel Density Estimation (KDE) and univariate/bivariate histograms using `sns.displot` and `sns.histplot`.
- **Pairwise Matrix Visualizations:** Correlation matrices via `sns.heatmap` and full-feature grid inspections via `sns.pairplot`.
- **Benchmark Datasets:** In-depth experimentation across real benchmark datasets (`tips`, `penguins`, `dots`, `titanic`, `iris`).

---

## 📁 Files & Notebooks Breakdown

| File | Type | Description |
|---|---|---|
| [`Creating_plots.ipynb`](Creating_plots.ipynb) | Jupyter Notebook | Complete guide to Seaborn figure-level and axes-level functions: theme configuration (`sns.set_theme`), built-in dataset discovery, color palettes, and facet grids. |
| [`Practice_problems.ipynb`](Practice_problems.ipynb) | Jupyter Notebook | Practical EDA drills on the `dots` and `tips` datasets exploring time-series relationships, firing rates, and customer tipping behavior. |
| [`Practice_problems1.ipynb`](Practice_problems1.ipynb) | Jupyter Notebook | Deep-dive exercises on multi-class distributions, bar charts with confidence intervals, and categorical counting. |
| [`Practice_problems2.ipynb`](Practice_problems2.ipynb) | Jupyter Notebook | Multi-attribute relational analysis on the `penguins` dataset comparing flipper length vs body mass grouped by island and species. |
| [`Plot_bill.py`](Plot_bill.py) | Python Script | Minimal standalone Python script demonstrating rapid scatter plot generation using `tips`. |

---

## 🛠️ Prerequisites & Installation

Install Seaborn alongside Matplotlib and Pandas:

```bash
pip install seaborn matplotlib pandas jupyter
```

---

## 🚀 How to Run

### Run the Standalone Script
```bash
python Seaborn/Plot_bill.py
```

### Launch Interactive Notebooks
```bash
jupyter notebook Seaborn/
```
- Open [`Creating_plots.ipynb`](Creating_plots.ipynb) for aesthetic styles and core functions.
- Open [`Practice_problems2.ipynb`](Practice_problems2.ipynb) for multi-variable feature distributions.

---

## 💡 Key Plotting Paradigms Demonstrated

### 1. High-Dimensional Relational Mapping
```python
import seaborn as sns

# Encode 4 dimensions simultaneously: x, y, color (hue), and marker style
sns.relplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    style="island"
)
```

### 2. Categorical Distribution & Outlier Detection
```python
# Compare total bills across days of the week with customer gender breakdown
sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    hue="sex",
    palette="Set2"
)
```
