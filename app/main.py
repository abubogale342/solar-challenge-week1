import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Solar Challenge Dashboard", layout="wide")

st.title("🌞 Solar Challenge Dashboard")

with st.sidebar:
    st.sidebar.header("Navigation")
    st.sidebar.write("Select a section from the sidebar.")

    country_list = list(['Benin', 'Togo', 'Sierraleon'])
    selected_year = st.selectbox('Select A Country', country_list)


# Sample data for demonstration
benin_cdf = pd.read_csv("./data/benin_clean.csv")
benin_cdf_head = benin_cdf.head(10)

togo_cdf = pd.read_csv("./data/togo_clean.csv")
togo_cdf_head = togo_cdf.head(10)

sierraleone_cdf = pd.read_csv("./data/sierraleone_clean.csv")
sierraleone_cdf_head = sierraleone_cdf.head(10)

def load_data(selected_year):
    if selected_year == 'Benin':
        return benin_cdf_head
    elif selected_year == 'Togo':
        return togo_cdf_head
    elif selected_year == 'Sierraleon':
        return sierraleone_cdf_head

loaded_cdf = load_data(selected_year)

st.subheader(f"GHI Boxplot for {selected_year}")

if "GHI" in loaded_cdf.columns:
    fig, ax = plt.subplots()
    sns.boxplot(y=loaded_cdf["GHI"], ax=ax)
    ax.set_title(f"GHI Boxplot for {selected_year}")
    st.pyplot(fig)
else:
    st.warning("GHI column not found in the data.")

st.subheader(f"Top 10 Cleaned {selected_year} Data")
st.dataframe(loaded_cdf)
