# Q - 7 Visualization Automation Tool 
# Create a script that: 
# - Accepts any dataset as input 
# - Generates a complete exploratory data analysis (EDA) report 
# - Automatically selects visualization types 
# - Includes statistical summaries alongside plots


import pandas as pd

def load_dataset(file_path):

    """Load dataset into pandas DataFrame"""
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
