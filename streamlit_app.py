import streamlit as st
import plotly.figure_factory as ff
import numpy as np

# Sample data (random values for demonstration)
data = np.random.randn(1000)

# Create a histogram using Plotly's create_distplot
fig = ff.create_distplot([data], ['Histogram'], bin_size=0.2)

# Set the layout for the chart
fig.update_layout(title='Histogram Example', xaxis_title='Values', yaxis_title='Frequency')

# Display the Plotly chart in the Streamlit app
st.plotly_chart(fig)
