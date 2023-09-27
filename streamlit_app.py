import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import pandas as pd

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


# Replace 'raw_csv_url' with the URL of the raw CSV file on GitHub
raw_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(raw_csv_url)
st.dataframe(df)