# SQL + Python Data Analysis

End-to-end data analysis: clean with Python / Pandas, query with SQL, check quality, and summarise findings.

Dataset is synthetic — an annotation QA log — so it can be shared publicly.

## What it does

- Loads and cleans a QA dataset
- Runs SQL-style checks (duplicates, missing values, accuracy by annotator)
- Produces a summary report: accuracy, throughput, error types

## Run it

```bash
pip install -r requirements.txt
python analysis.py
```

SQL queries are in `queries.sql` — run them in MySQL / PostgreSQL / SQLite.

## Files

- `analysis.py` — Pandas cleaning + analysis
- `queries.sql` — QA queries: accuracy by annotator, error rate by category
- `data/annotation_qa_sample.csv` — synthetic sample data
- `report.md` — example findings

## Skills demonstrated

Python (Pandas, NumPy), SQL, ETL, data quality checks, Tableau / Power BI-ready outputs.
