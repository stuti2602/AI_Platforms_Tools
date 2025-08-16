import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def handle_missing_values(df, strategy):
    if strategy == "mean":
        df = df.fillna(df.mean(numeric_only=True))
        return df, "Missing values filled with column mean."
    elif strategy == "median":
        df = df.fillna(df.median(numeric_only=True))
        return df, "Missing values filled with column median."
    elif strategy == "drop":
        df = df.dropna()
        return df, "Dropped rows with missing values."
    else:
        return df, "No missing value handling applied."

def remove_outliers(df):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    logs = []
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR
        before = len(df)
        df = df[(df[col] >= lower) & (df[col] <= upper)]
        after = len(df)
        logs.append(f"Removed outliers in '{col}': {before - after} rows dropped.")
    return df, logs

def scale_features(df, method):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if method == "standard":
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        return df, "Applied Standard Scaling (mean=0, std=1)."
    elif method == "normalize":
        scaler = MinMaxScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        return df, "Applied Min-Max Normalization (0-1 range)."
    return df, "No scaling applied."
