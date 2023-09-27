import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data
data = {'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 20, 15, 25]}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a Plotly figure using Plotly Express
fig = px.bar(df, x='Category', y='Value', title='Sample Bar Chart')

# Display the Plotly chart in the Streamlit app
st.plotly_chart(fig)
