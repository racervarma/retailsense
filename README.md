\# 🛒 RetailSense: End-to-End Data Analysis \& Insights Dashboard



\## Project Overview

RetailSense is an end-to-end data analysis pipeline and dashboard for a fictional retail company. This project involves data cleaning, SQL/Pandas analysis, API integration, and an interactive Streamlit dashboard.



\## Project Structure

\- `data/`: Raw CSV datasets (customers, orders, products).

\- `outputs/`: Cleaned datasets, reports, JSON data, and SQLite database.

\- `notebooks/`: Jupyter notebooks for exploratory data analysis (EDA) and SQL querying.

\- `app.py`: Interactive Streamlit dashboard.

\- `utils.py`: Reusable Python functions for data processing.

\- `config.json`: Configuration variables.



\## Setup Instructions

1\. Run `python run\_once\_generate\_data.py` to generate the raw CSV files in the `data/` folder.

2\. Ensure you have the required packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`, `requests`, `streamlit`.

3\. Run the analysis in `notebooks/analysis.ipynb`.

4\. Launch the dashboard using: `streamlit run app.py`

