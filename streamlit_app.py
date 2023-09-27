import streamlit as st
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import requests


# GitHub CSV file URL
github_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'

# Function to fetch and load CSV data
@st.cache
def load_data(url):
    response = requests.get(url)
    data = pd.read_csv(response.text)
    return data

# Load CSV data
data = load_data(github_csv_url)

# Display the loaded data
st.write(data)

# Sample data (random values for demonstration)
data = np.random.randn(1000)

# Create a histogram using Plotly's create_distplot
fig = ff.create_distplot([data], ['Histogram'], bin_size=0.2)

# Set the layout for the chart
fig.update_layout(title='Histogram Example', xaxis_title='Values', yaxis_title='Frequency')

# Display the Plotly chart in the Streamlit app
st.plotly_chart(fig)
