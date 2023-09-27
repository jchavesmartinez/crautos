import pandas as pd
import streamlit as st
import plotly.figure_factory as ff


github_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'

# Use pandas to read the CSV file from the URL
df = pd.read_csv(github_csv_url, encoding='latin-1')

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6, 6, 6]

fig = ff.create_distplot(
        data,  bin_size=[.1, .25, .5])

st.plotly_chart(fig, use_container_width=True)