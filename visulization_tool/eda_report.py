import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_eda_report(df):
    """Generate a simple EDA report with stats + visualizations"""
    
    # 1. Basic Info
    print("\nDataset Info:")
    print(df.info())
    print("\nSummary Statistics:")
    print(df.describe())

    # 2. Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # 3. Visualizations
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

    for col in df.select_dtypes(include=['object']).columns:
        plt.figure(figsize=(6, 4))
        sns.countplot(y=df[col])
        plt.title(f"Category Counts of {col}")
        plt.show()
