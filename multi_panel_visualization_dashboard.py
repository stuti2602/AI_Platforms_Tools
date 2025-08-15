# Q-4  Multi-Panel Visualization Dashboard 
# Build a dashboard using matplotlib and seaborn that: 
# - Supports different data types 
# - Automatically selects suitable chart types 
# - Displays multiple panels for comparison 
# - Includes legends, titles, and annotations for clarity


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def multi_panel_dashboard(df):
    # Separate numeric and categorical columns
    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(exclude='number').columns

    # Create figure with multiple panels
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Multi-Panel Visualization Dashboard", fontsize=16, fontweight='bold')

    # Numeric column distribution (Histogram)
    if len(numeric_cols) > 0:
        sns.histplot(df[numeric_cols[0]], bins=10, ax=axes[0, 0], kde=True)
        axes[0, 0].set_title(f"Distribution of {numeric_cols[0]}")
        axes[0, 0].set_xlabel(numeric_cols[0])
        axes[0, 0].set_ylabel("Frequency")
    else:
        axes[0, 0].text(0.5, 0.5, "No Numeric Data", ha='center', va='center')

    # Numeric vs Numeric (Scatter Plot)
    if len(numeric_cols) >= 2:
        sns.scatterplot(x=df[numeric_cols[0]], y=df[numeric_cols[1]], ax=axes[0, 1])
        axes[0, 1].set_title(f"{numeric_cols[0]} vs {numeric_cols[1]}")
    else:
        axes[0, 1].text(0.5, 0.5, "Not Enough Numeric Data", ha='center', va='center')

    # Categorical count plot
    if len(categorical_cols) > 0:
        sns.countplot(x=df[categorical_cols[0]], ax=axes[1, 0])
        axes[1, 0].set_title(f"Count of {categorical_cols[0]}")
        axes[1, 0].set_xlabel(categorical_cols[0])
    else:
        axes[1, 0].text(0.5, 0.5, "No Categorical Data", ha='center', va='center')

    # Boxplot for outlier visualization
    if len(numeric_cols) > 0:
        sns.boxplot(y=df[numeric_cols[0]], ax=axes[1, 1])
        axes[1, 1].set_title(f"Boxplot of {numeric_cols[0]}")
    else:
        axes[1, 1].text(0.5, 0.5, "No Numeric Data", ha='center', va='center')

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Leave space for main title
    plt.show()

def main():
    # Example dataset
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"],
        "Age": [25, 30, 35, 40, 29, 31, 38],
        "Salary": [50000, 60000, 75000, 80000, 58000, 62000, 79000],
        "Department": ["HR", "IT", "IT", "Finance", "Finance", "HR", "IT"]
    }
    df = pd.DataFrame(data)

    multi_panel_dashboard(df)

if __name__ == "__main__":
    main()

    
