import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import pandas as pd


github_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'

# Use pandas to read the CSV file from the URL
df = pd.read_csv(github_csv_url, encoding='latin-1')

# Sample data (random values for demonstration)
data = np.random.randn(1000)

# Create a histogram using Plotly's create_distplot
fig = ff.create_distplot([data], ['Histogram'], bin_size=0.2)

# Set the layout for the chart
fig.update_layout(title='Histogram Example', xaxis_title='Values', yaxis_title='Frequency')

# Display the Plotly chart in the Streamlit app
st.plotly_chart(fig)
