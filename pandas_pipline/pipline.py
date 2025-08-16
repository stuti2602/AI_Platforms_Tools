# Q - 6 pandas Data Transformation Pipeline 
# Implement a configurable pipeline that: 
# - Handles missing values with various strategies 
# - Detects and removes outliers 
# - Performs feature scaling (normalization, standardization) 
# - Logs each transformation step 

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from utils import handle_missing_values, remove_outliers, scale_features

class DataTransformationPipeline:
    def __init__(self, missing_strategy="mean", scaling_method="standard"):
        """
        missing_strategy: 'mean', 'median', 'drop'
        scaling_method: 'standard', 'normalize', None
        """
        self.missing_strategy = missing_strategy
        self.scaling_method = scaling_method
        self.log = []

    def transform(self, df):
        """Run full pipeline on DataFrame"""
        df, log1 = handle_missing_values(df, self.missing_strategy)
        self.log.append(log1)

        df, log2 = remove_outliers(df)
        self.log.extend(log2)

        df, log3 = scale_features(df, self.scaling_method)
        self.log.append(log3)

        return df

    def get_logs(self):
        return self.log
