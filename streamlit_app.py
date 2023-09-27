import pandas as pd
import streamlit as st


github_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'

# Use pandas to read the CSV file from the URL
df = pd.read_csv(github_csv_url, encoding='latin-1')

#st.table(df)