# EduPro Learner Analytics

## Project Overview

This project analyzes learner demographics and enrollment behavior on the EduPro online learning platform using Python, Pandas, Plotly, Seaborn, and Streamlit.

## Objectives

- Analyze learner demographics
- Study enrollment patterns
- Identify course popularity
- Compare learner preferences across age and gender
- Build an interactive analytics dashboard

## Dataset

Three datasets are used:

- Users
- Courses
- Transactions

## Technologies

- Python
- Pandas
- NumPy
- Plotly
- Seaborn
- Streamlit

## Dashboard

Run `streamlit run dashboard/app.py` from the repository root.

## Installation

pip install -r requirements.txt

streamlit run dashboard/app.py

## Project Structure

The repository follows the requested `data/`, `notebooks/`, `src/`, `dashboard/`, and `reports/` layout. The included CSVs are a small, synthetic starter dataset; replace them with approved source data using the same columns.

## Results

- Age distribution
- Gender participation
- Course popularity
- Heatmaps
- KPIs

## Data pipeline

Run `python -m src.preprocessing` to clean and merge the three raw CSV files into `data/processed/merged_data.csv`. The notebooks provide a guided version of the same workflow.
