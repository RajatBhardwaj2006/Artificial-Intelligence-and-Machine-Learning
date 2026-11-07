# Data Collection: Web Scraping & REST APIs

A practical guide and code repository dedicated to extracting, parsing, and structuring raw data from web sources and RESTful APIs using Python, **BeautifulSoup4**, **Requests**, and **Pandas**.

---

## 📌 Overview

Data collection is the foundation of data science and machine learning. This module demonstrates real-world workflows for gathering structured data:
- **HTML Parsing & Tag Extraction:** Navigating the DOM tree, CSS selectors, attributes, and sibling nodes.
- **Paginated Web Scraping:** Programmatically crawling multi-page sites (e.g., quotes datasets) and archiving HTML snapshots.
- **REST API Consumption:** Interacting with JSON endpoints, status code verification, and error handling.
- **Data Structuring & Cleaning:** Exporting unstructured web content into tidy CSV datasets ready for analytics.

---

## 📁 Directory Structure & File Index

| File / Folder | Type | Description |
|---|---|---|
| [`Activity_1.ipynb`](Activity_1.ipynb) | Jupyter Notebook | Complete project pipeline: Crawls paginated pages from `quotes.toscrape.com`, parses local HTML files, filters quotes tagged with `"life"`, extracts author metadata, and structures results with Pandas. |
| [`BeatifulSoup.ipynb`](BeatifulSoup.ipynb) | Jupyter Notebook | Tutorial on BeautifulSoup basics: finding elements (`find`, `find_all`), navigating relative nodes (`find_next`), stripping whitespace, extracting country population lists, and compiling data tables. |
| [`Working_with_API.ipynb`](Working_with_API.ipynb) | Jupyter Notebook | Hands-on API integration: fetching data from REST endpoints (Stephen King books API, Cat Facts API, ScrapeThisSite endpoints), inspecting JSON responses, and error-handling status codes. |
| [`Scrape_Links.py`](Scrape_Links.py) | Python Script | Lightweight utility for extracting and resolving all absolute hyperlinks (`href`) from web pages using `urllib.parse.urljoin`. |
| [`Cleaned_data.csv`](Cleaned_data.csv) | Dataset | Cleaned tabular dataset of world countries and population figures extracted from web scraping exercises. |
| [`Web_Scrapping/`](Web_Scrapping/) | Directory | Local offline cache containing raw HTML page snapshots (`Quotes1.html` to `Quotes10.html`) for reproducible offline scraping practice. |

---

## 🛠️ Prerequisites & Installation

Install the required Python libraries:

```bash
pip install requests beautifulsoup4 pandas jupyter
```

---

## 🚀 Execution & Usage

### 1. Extract Links from a Web Page
```bash
python Data_Collection/Scrape_Links.py
```

### 2. Run the Interactive Notebooks
Launch Jupyter Notebook or Jupyter Lab:
```bash
jupyter notebook Data_Collection/
```
- Open [`BeatifulSoup.ipynb`](BeatifulSoup.ipynb) to learn element querying.
- Open [`Activity_1.ipynb`](Activity_1.ipynb) to review paginated scraping pipelines.
- Open [`Working_with_API.ipynb`](Working_with_API.ipynb) to practice API request workflows.

---

## 💡 Key Techniques & Best Practices

1. **Local HTML Caching:** Saving downloaded HTML files during large scrapes avoids overloading remote servers and ensures reproducible offline testing.
2. **Defensive Requesting:** Always validating HTTP response statuses (`response.raise_for_status()` or `response.status_code == 200`) and configuring network timeouts.
3. **URL Resolution:** Utilizing `urllib.parse.urljoin` to safely resolve relative hyperlinks (`/author/einstein`) into fully-qualified URLs.
4. **Resilient Selectors:** Preferring semantic CSS selectors (`soup.select(".quote .text")`) over fragile absolute XPath positions.
