import pandas as pd
import streamlit as st
import plotly.figure_factory as ff

# Replace 'raw_csv_url' with the URL of the raw CSV file on GitHub
raw_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'

try:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(raw_csv_url, encoding='latin-1')
    
    # Display the DataFrame using Streamlit
    st.dataframe(df)

    # Add histogram data
    x1 = df['Grupo de años'].values
    x2 = df['MarcaModelo'].values
    x3 = df['Precio'].values

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
