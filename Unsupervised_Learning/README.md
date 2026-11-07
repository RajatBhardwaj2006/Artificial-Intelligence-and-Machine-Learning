# Unsupervised Machine Learning: Clustering, Dimensionality Reduction & Anomaly Detection

A comprehensive laboratory dedicated to **Unsupervised Machine Learning**, covering centroid-based clustering (K-Means), density-based clustering (DBSCAN), hierarchical agglomerative clustering with dendrograms, Principal Component Analysis (PCA), and spatial anomaly detection.

---

## 📌 Overview

Unsupervised learning discovers intrinsic patterns, structural groupings, and latent manifolds within unlabeled data ($\mathbf{X}$):
- **Centroid-Based Clustering (K-Means):** Partitioning observations into $K$ voronoi cells by iteratively updating cluster centroids to minimize within-cluster sum-of-squares (Inertia).
- **Density-Based Spatial Clustering (DBSCAN):** Discovering arbitrary-shaped clusters and filtering spatial noise based on core-point density thresholds ($\epsilon$ and `min_samples`).
- **Hierarchical Clustering:** Bottom-up agglomerative tree construction visualized through dendrogram diagrams to inspect taxonomic linkages.
- **Dimensionality Reduction (PCA):** Orthogonal linear projection onto principal eigenvectors that maximize captured variance while compressing feature dimensions.
- **Anomaly & Outlier Detection:** Pinpointing anomalous points that deviate from expected cluster densities.

---

## 📁 Notebooks & Algorithmic Index

| Notebook | Paradigm | Core Concepts & Techniques |
|---|---|---|
| [`KMeans.ipynb`](KMeans.ipynb) | Centroid Clustering | Synthetic isotropic Gaussian blobs (`make_blobs`), Elbow Method (Inertia vs. $K$), Silhouette Score validation, and cluster centroid tracking. |
| [`DBSCAN.ipynb`](DBSCAN.ipynb) | Density Clustering | Non-linear geometric shapes (`make_moons`), standard scaling, core point / border point distinction, and handling irregular noise clusters without specifying $K$ upfront. |
| [`AnomalyDetection.ipynb`](AnomalyDetection.ipynb) | Outlier Detection | Detecting out-of-distribution points and anomalous density deviations on non-linear distributions and synthetic manifolds. |
| [`hierarchical_cluster.ipynb`](hierarchical_cluster.ipynb) | Hierarchical Clustering | Agglomerative clustering on the Iris dataset, computing Euclidean linkage matrices, dendrogram tree plotting with SciPy, and cluster pruning. |
| [`PCA.ipynb`](PCA.ipynb) | Dimensionality Reduction | Covariance matrix eigen-decomposition, explained variance ratio analysis, and high-to-low dimensional projection for 2D/3D feature visualizers. |

---

## 🧠 Algorithmic Taxonomy & Comparison

| Algorithm | Type | Geometry / Shape | Requires $K$? | Noise / Outlier Handling |
|---|---|---|---|---|
| **K-Means** | Centroid-based | Spherical / convex clusters | Yes | Sensitive to outliers |
| **DBSCAN** | Density-based | Arbitrary / non-linear shapes | No | Explicitly labels noise as `-1` |
| **Hierarchical** | Tree / Connectivity | Multi-scale taxonomic structures | Optional (cut dendrogram) | Grouped into small outlier leaves |
| **PCA** | Linear Projection | Variance-maximizing linear subspace | Select $n\_components$ | Reconstructs residuals to flag anomalies |

---

## 🛠️ Prerequisites & Installation

Install the machine learning and scientific visualization stack:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn scipy jupyter
```

---

## 🚀 How to Run the Experiments

Launch Jupyter Notebook:

```bash
jupyter notebook Unsupervised_Learning/
```

- Open [`KMeans.ipynb`](KMeans.ipynb) to inspect the WCSS Elbow Curve and optimal cluster selection.
- Open [`DBSCAN.ipynb`](DBSCAN.ipynb) to see how density clustering resolves interleaving half-moons.
- Open [`hierarchical_cluster.ipynb`](hierarchical_cluster.ipynb) to view dendrogram linkage plots.
- Open [`PCA.ipynb`](PCA.ipynb) to visualize high-dimensional compression.

---

## 💡 Practical Machine Learning Workflows

### 1. Determining Optimal $K$ via the Elbow Curve
```python
from sklearn.cluster import KMeans

wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
```

### 2. Dimensionality Reduction with PCA
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
```
