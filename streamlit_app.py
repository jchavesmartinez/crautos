import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
from pandas import json_normalize
import plotly.figure_factory as ff


path= "https://raw.githubusercontent.com/jchavesmartinez/StreamlitBudget/main/Budget.csv"
Budget2023 = pd.read_csv(path, encoding='latin-1',index_col=0)

with st.expander("Presupuesto 2023"):
    st.dataframe(Budget2023,use_container_width=True)
    
    

# Sample data (random values for demonstration)
data = np.random.randn(1000)

# Create a histogram using Plotly's create_distplot
fig = ff.create_distplot([data], ['Histogram'], bin_size=0.2)

# Set the layout for the chart
fig.update_layout(title='Histogram Example', xaxis_title='Values', yaxis_title='Frequency')

# Display the Plotly chart in the Streamlit app
st.plotly_chart(fig)