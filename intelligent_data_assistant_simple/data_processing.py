import pandas as pd

def get_numeric_summary(df):
    return df.select_dtypes(include=['number']).columns.tolist()

def get_text_columns(df):
    return df.select_dtypes(include=['object']).columns.tolist()
