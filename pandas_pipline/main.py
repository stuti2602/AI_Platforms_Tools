import pandas as pd
from pipline import DataTransformationPipeline

if __name__ == "__main__":
    # Sample dataset
    data = {
        "Age": [25, 30, None, 120, 40, 35],
        "Salary": [50000, 60000, 70000, 800000, 55000, None],
        "Dept": ["IT", "HR", "IT", "Finance", "HR", "IT"]
    }

    df = pd.DataFrame(data)
    print("\nOriginal Data:")
    print(df)

    # Create pipeline
    pipeline = DataTransformationPipeline(missing_strategy="mean", scaling_method="normalize")
    transformed_df = pipeline.transform(df)

    print("\nTransformed Data:")
    print(transformed_df)

    print("\nLog of steps:")
    for step in pipeline.get_logs():
        print(step)
