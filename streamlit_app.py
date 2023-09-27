import pandas as pd
import streamlit as st
import plotly.express as px


github_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'

# Use pandas to read the CSV file from the URL
df = pd.read_csv(github_csv_url, encoding='latin-1')

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6]
fig = px.histogram(data, nbins=5, title="Sample Histogram")