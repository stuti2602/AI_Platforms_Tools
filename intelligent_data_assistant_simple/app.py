

import streamlit as st
import pandas as pd
from data_processing import get_numeric_summary, get_text_columns
from visualization import plot_numeric
from nlp_module import extract_keywords
from ai_integration import get_sentiment
from report_generator import generate_report

st.title("Intelligent Data Assistant - Modular Version")
uploaded = st.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df.head())

    # Numeric summary & plots
    numeric_cols = get_numeric_summary(df)
    st.write(df[numeric_cols].describe())
    if numeric_cols:
        plot_numeric(df, numeric_cols[0])

    # NLP
    text_cols = get_text_columns(df)
    if text_cols:
        top_keywords = extract_keywords(df, text_cols[0])
        st.write("Top keywords:", top_keywords)
        sentiments = get_sentiment(df, text_cols[0])
        st.write("Sentiment Analysis:", sentiments)

    # Report
    report_text = generate_report(df, numeric_cols, text_cols, top_keywords)
    st.text_area("Report", value=report_text, height=200)
