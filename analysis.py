"""SQL + Python data analysis - annotation QA (synthetic data).
Run: python analysis.py
"""
import pandas as pd

df = pd.read_csv("data/annotation_qa_sample.csv")
print(f"Rows: {len(df)} | Annotators: {df['annotator'].nunique()}")
print("\nAccuracy by annotator:")
print(df.groupby("annotator")["correct"].mean().round(2))
print("\nError rate by category:")
print(df.groupby("category")["correct"].apply(lambda s: 1 - s.mean()).round(2))
print("\nMissing values:")
print(df.isna().sum())
df.to_csv("cleaned_qa.csv", index=False)
print("\nWrote cleaned_qa.csv")
