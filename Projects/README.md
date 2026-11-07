# Machine Learning & AI Capstone Projects Portfolio

A portfolio of end-to-end Machine Learning, Deep Learning, Unsupervised Clustering, and GenAI applications developed by **Rajat Bhardwaj**. Each project contains complete data pipelines, exploratory data analysis, feature engineering, model training, evaluation metrics, and interactive user interfaces.

---

## 📌 Portfolio Overview

| Project | Domain | Paradigm | Tech Stack | Highlights |
|---|---|---|---|---|
| [**CreditWise Loan System**](#1-creditwise-loan-approval-system) | FinTech / Risk Assessment | Supervised Classification | Scikit-Learn, Pandas, Seaborn | Predicts loan defaults and approval status using financial history and risk features. |
| [**SmartCart Cluster System**](#2-smartcart-customer-segmentation-system) | Retail / E-Commerce | Unsupervised Learning | K-Means, PCA, Matplotlib, Seaborn | Segments retail shoppers by spending score and annual income using the Elbow Method and Silhouette Analysis. |
| [**House Price Predictor**](#3-house-price-prediction) | Real Estate Valuation | Supervised Regression | Scikit-Learn, NumPy, Pandas | Continuous valuation regression handling missing values, encoding, and RMSE minimization. |
| [**Iris Species Classifier**](#4-iris-flower-species-classification) | Botany / Benchmark | Multi-Class Classification | KNN, Decision Trees, SVM | Benchmark study comparing parametric and non-parametric decision boundaries. |
| [**YouTube Video Analyzer**](#5-youtube-video-analyzer-agent) | Generative AI & Video Intel | Agentic LLM / NLP | Streamlit, Agno, Groq LLM | Extracts video transcripts, calculates timestamp boundaries, and generates structured executive briefings. |

---

## 📁 Project Architecture & Deep Dives

### 1. CreditWise Loan Approval System
- **Directory:** [`CreditWise_Loan_System/`](CreditWise_Loan_System/)
- **Core Files:**
  - [`LoanSystem.ipynb`](CreditWise_Loan_System/LoanSystem.ipynb): Full modeling notebook with data imputation, scaling, train/test splitting, and classification benchmarks.
  - [`CreditWise Loan System.pdf`](CreditWise_Loan_System/CreditWise%20Loan%20System.pdf): Comprehensive project documentation and risk analysis methodology.
  - [`loan_approval_data.csv`](CreditWise_Loan_System/loan_approval_data.csv): Historical applicant dataset including credit scores, income, assets, and loan outcomes.
- **Key Concepts:** Missing data imputation (`SimpleImputer`), class balance evaluation, confusion matrices, Precision-Recall trade-offs, and ROC-AUC scoring.

---

### 2. SmartCart Customer Segmentation System
- **Directory:** [`SmartCart_Cluster_system/`](SmartCart_Cluster_system/)
- **Core Files:**
  - [`SmartCart.ipynb`](SmartCart_Cluster_system/SmartCart.ipynb): Unsupervised learning pipeline for customer clustering.
  - [`smartcart_customers.csv`](SmartCart_Cluster_system/smartcart_customers.csv): Customer profile dataset detailing demographic factors, annual income, and spending scores.
- **Key Concepts:** Determining optimal cluster count $K$ via the WCSS (Within-Cluster Sum of Squares) Elbow Curve, silhouette validation, 2D/3D cluster scatter visualizers, and marketing persona profiling.

---

### 3. House Price Prediction
- **Directory:** [`Minor_Projects/House_price/`](Minor_Projects/House_price/)
- **Core Files:**
  - [`house_price_predictor.ipynb`](Minor_Projects/House_price/house_price_predictor.ipynb): Predictive regression pipeline.
  - [`HousePricePrediction.csv`](Minor_Projects/House_price/HousePricePrediction.csv): Property sales records with physical attributes, living area, year built, and sale prices.
- **Key Concepts:** Feature engineering, handling multicollinearity, standard scaling, and regression metric evaluation ($R^2$, Mean Absolute Error, Root Mean Squared Error).

---

### 4. Iris Flower Species Classification
- **Directory:** [`Minor_Projects/Iris_flower/`](Minor_Projects/Iris_flower/)
- **Core Files:**
  - [`iris_Flower.ipynb`](Minor_Projects/Iris_flower/iris_Flower.ipynb): Multi-class classification experiment.
  - [`Iris.csv`](Minor_Projects/Iris_flower/Iris.csv): Morphological measurement dataset across Setosa, Versicolor, and Virginica classes.
- **Key Concepts:** Decision tree depth tuning, K-Nearest Neighbors hyperparameter $k$ selection, and cross-validated accuracy assessment.

---

### 5. YouTube Video Analyzer Agent
- **Directory:** [`Youtube_video_analyzer/`](Youtube_video_analyzer/)
- **Core Files:**
  - [`analyzer.py`](Youtube_video_analyzer/analyzer.py): Autonomous Agno agent powered by Groq LLM and YouTube transcript extraction tools.
  - [`ui.py`](Youtube_video_analyzer/ui.py): Interactive Streamlit web interface for submitting URLs and rendering formatted markdown summaries.
- **Key Concepts:** LLM tool calling, transcript segmentation, hallucination prevention in timestamps, and generative markdown report generation.

---

## 🛠️ Environment Setup & Installation

Clone the parent repository and install project dependencies:

```bash
git clone https://github.com/RajatBhardwaj2006/Artificial-Intelligence-and-Machine-Learning.git
cd Artificial-Intelligence-and-Machine-Learning

pip install numpy pandas scikit-learn matplotlib seaborn jupyter streamlit agno groq youtube-transcript-api python-dotenv
```

---

## 🚀 How to Run the Applications

### 1. Launch Jupyter Notebook for ML Pipelines
```bash
jupyter notebook Projects/
```
Navigate into any subproject folder (`CreditWise_Loan_System`, `SmartCart_Cluster_system`, or `Minor_Projects`) to execute notebook cells sequentially.

### 2. Launch the Streamlit YouTube Video Analyzer
```bash
# Ensure GROQ_API_KEY is configured in your .env
streamlit run Projects/Youtube_video_analyzer/ui.py
```
Open your browser at `http://localhost:8501` to use the interactive video intelligence dashboard.
