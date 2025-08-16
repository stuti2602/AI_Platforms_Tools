from data_loader import load_dataset
from eda_report import generate_eda_report

def main():
    # Change file path to your dataset
    file_path = "C:/Data/Dotconnect_Workshop_Repos/code_for_api/AI_Platforms_Tools/visulization_tool/titanic.csv"
    df = load_dataset(file_path)

    if df is not None:
        generate_eda_report(df)

if __name__ == "__main__":
    main()
