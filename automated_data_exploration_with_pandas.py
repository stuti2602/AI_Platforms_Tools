# Q-3 Automated Data Exploration with pandas 
# Create a reusable function or class that:
# - Generates statistical summaries for each column 
# - Detects and reports missing values, duplicates, and outliers 
# - Recommends preprocessing steps 
# - Outputs a well-structured report


import pandas as pd

def automated_data_exploration(job_table):
    print("===== DATA EXPLORATION REPORT =====\n")

    # Basic statistical summary
    print("Statistical Summary:")
    print(job_table.describe(include='all'))
    print("\n")

    # Missing values
    print("Missing Values:")
    missing = job_table.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values")
    print("\n")

    # Duplicate rows
    print("Duplicate Rows:")
    duplicate_count = job_table.duplicated().sum()
    print(f"Total Duplicates: {duplicate_count}")
    print("\n")

    # Outlier detection (simple IQR method for numeric columns)
    print("Outlier Detection:")
    numeric_cols = job_table.select_dtypes(include='number').columns
    for col in numeric_cols:
        Q1 = job_table[col].quantile(0.25)
        Q3 = job_table[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = job_table[(job_table[col] < Q1 - 1.5 * IQR) | (job_table[col] > Q3 + 1.5 * IQR)]
        if not outliers.empty:
            print(f"{col}: {len(outliers)} outliers detected")
    print("\n")

    # Recommendations
    print("Recommended Preprocessing Steps:")
    if missing.sum() > 0:
        print("- Fill or drop missing values")
    if duplicate_count > 0:
        print("- Remove duplicate rows")
    print("- Scale numeric features if using ML models")
    print("- Encode categorical variables if needed")
    print("\n===== END OF REPORT =====")



def main():

        # Example dataset
    data = {
        "Name": ["Alice", "Bob", "Charlie", "Bob", None],
        "Age": [25, 30, 35, 30, 120],
        "Salary": [50000, 60000, 75000, 60000, None]
    }
    job_table = pd.DataFrame(data)

    automated_data_exploration(job_table)


if __name__ == "__main__":
    main()

