import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px


# Replace 'raw_csv_url' with the URL of the raw CSV file on GitHub


try:

    st.title('Portal de inversión carros Costa Rica')

    @st.cache
    def load_data():
        # Load or compute your data here (e.g., from a CSV file)
        raw_csv_url = 'https://raw.githubusercontent.com/jchavesmartinez/crautos/main/MASTERDATA%20-%20LIMPIA.csv'
        df = pd.read_csv(raw_csv_url, encoding='latin-1')
        return df

    # Load the data using the cached function
    df = load_data()

    
    tab1, tab2 = st.tabs(["Metricas del mercado", "Potenciales inversiones"])
    
    with tab1:
    
        col1, col2, col3 = st.columns(3)

        with col1:
            # Create a sample DataFrame (replace this with your 'df' from the CSV)
            data = {'values': df['Marca'].values}
            df = pd.DataFrame(data)

            # Create a histogram using Plotly Express
            fig = px.histogram(df, x='values', nbins=10, title='Histogram')

            fig.update_layout(
                plot_bgcolor='white',  # Background color of the plot area
                paper_bgcolor='white'  # Background color of the entire figure
            )

            # Display the histogram in the Streamlit app
            st.plotly_chart(fig)

        with col2:
            st.header("A dog")
            st.image("https://static.streamlit.io/examples/dog.jpg")


except Exception as e:
    st.error(f"An error occurred: {str(e)}")
