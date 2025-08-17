def generate_report(df, numeric_cols, text_cols, top_keywords):
    report = f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n"
    report += f"Numeric columns: {numeric_cols}\nText columns: {text_cols}\n"
    report += f"Top keywords: {top_keywords[:5]}"
    return report
