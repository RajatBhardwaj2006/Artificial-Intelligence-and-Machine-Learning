# Data Visualization with Matplotlib

A comprehensive, hands-on repository of **Matplotlib** visualizations and statistical plotting techniques tailored for Exploratory Data Analysis (EDA), business intelligence, and Machine Learning diagnostics.

---

## 📌 Overview

Visualizing data is crucial for pattern detection, outlier identification, and model evaluation. This folder covers:
- **Distribution Analysis:** Histograms, KDEs, and Box Plots (IQR, quartiles, and whiskers).
- **Relational & Correlation Visualizations:** Scatter plots with annotations, regressions, and multi-variable coloring.
- **Categorical & Compositional Visualizations:** Bar charts, pie charts, donut charts, and stack plots.
- **Time Series & Trend Analysis:** Multi-line plots with dual axes, fills, and custom legends.
- **ML Diagnostics:** Plotting training vs. validation loss/accuracy curves to detect overfitting and underfitting.
- **Modern Matplotlib Styling:** Figure and axes object-oriented API (`fig, ax = plt.subplots()`), custom spines, grids, annotations, and palettes.

---

## 📁 Notebooks & Scripts Index

| File | Type | Description |
|---|---|---|
| [`Bar_chart.ipynb`](Bar_chart.ipynb) | Jupyter Notebook | Vertical, horizontal, grouped, and stacked bar charts for categorical feature comparison. |
| [`Box_plot.ipynb`](Box_plot.ipynb) | Jupyter Notebook | Box-and-whisker plots depicting median, interquartile range (IQR), variance, and anomaly/outlier detection. |
| [`Histogram.ipynb`](Histogram.ipynb) | Jupyter Notebook | Frequency distributions, binning strategies, cumulative histograms, and density estimations. |
| [`line_plot.ipynb`](line_plot.ipynb) | Jupyter Notebook | Continuous trends over time, styling linestyles, markers, legends, and grid customizations. |
| [`Pie_chart.ipynb`](Pie_chart.ipynb) | Jupyter Notebook | Proportional representation, exploding slices, autopct formatting, and donut chart implementations. |
| [`Scatter_plots.ipynb`](Scatter_plots.ipynb) | Jupyter Notebook | Bi-variate relationship analysis, bubble charts (encoding 3rd dimension via size/color), and trendlines. |
| [`Stack_plot.ipynb`](Stack_plot.ipynb) | Jupyter Notebook | Area charts and stacked area plots comparing part-to-whole progressions over time (`baseline="zero"`, `"sym"`, `"wiggle"`). |
| [`modern_PLT.ipynb`](modern_PLT.ipynb) | Jupyter Notebook | Best-practice modern Matplotlib styling, subplots grids, spine removal, typography, and dark/light themes. |
| [`plot_train_valid.ipynb`](plot_train_valid.ipynb) | Jupyter Notebook | Machine learning metric curves: visual comparison of training vs validation loss/accuracy to identify overfitting/early stopping points. |
| [`ano.py`](ano.py) | Python Script | Demonstrates point annotation (`plt.annotate`) with custom arrows and red callouts for identifying anomalies. |
| [`practice.py`](practice.py) | Python Script | Rapid prototyping script for stack plots with baseline configurations (`zero`, `sym`, `wiggle`). |

---

## 🛠️ Prerequisites & Installation

Install the required visualization and scientific computing libraries:

```bash
pip install matplotlib numpy pandas jupyter
```

---

## 🚀 How to Run

Launch the interactive Jupyter interface:

```bash
jupyter notebook Matplotlib/
```

Or execute standalone Python demonstration scripts:

```bash
python Matplotlib/ano.py
python Matplotlib/practice.py
```

---

## 💡 Visualization Best Practices

1. **Object-Oriented API:** Prefer `fig, ax = plt.subplots()` over stateful `plt.plot()` calls for full control over subplots and axis formatting.
2. **High Data-to-Ink Ratio:** Remove distracting chart junk (unnecessary top/right borders, excessively heavy gridlines).
3. **Readable Annotations:** Use `ax.annotate()` to highlight key business turning points or anomalous outliers.
4. **Color Accessibility:** Utilize colorblind-safe colormaps (e.g., `viridis`, `plasma`) rather than saturated raw primaries.
