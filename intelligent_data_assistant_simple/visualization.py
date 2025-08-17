import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_numeric(df, col):
    st.subheader(f"Histogram for {col}")
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    st.pyplot(fig)
