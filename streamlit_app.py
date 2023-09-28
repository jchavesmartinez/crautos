import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px


# Replace 'raw_csv_url' with the URL of the raw CSV file on GitHub

# Use st.set_page_config to configure the layout
st.set_page_config(
    layout="wide",  # Set the layout to "wide"
    page_title="Portal de inversiones autos",  # Set the title of the app
)

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
    
        with st.expander("See explanation"):
            st.write('WENAS')
            st.image("https://static.streamlit.io/examples/dice.jpg")
    
    
        col1, col2 = st.columns([1, 1])

        with col1:
            # Create a sample DataFrame (replace this with your 'df' from the CSV)
            data1 = {'values': df['Marca'].values}
            df1 = pd.DataFrame(data1)

            # Create a histogram using Plotly Express
            fig1 = px.histogram(df1, x='values', nbins=10, title='Histogram')

            fig1.update_layout(
                plot_bgcolor='white',  # Background color of the plot area
                paper_bgcolor='white'  # Background color of the entire figure
            )

            # Display the histogram in the Streamlit app
            fig1.update_layout(width=1200, height=500)
            st.plotly_chart(fig1)


        with col2:
            # Create a sample DataFrame (replace this with your 'df' from the CSV)
            data2 = {'values': df['Grupo de años'].values}
            df2 = pd.DataFrame(data2)

            # Create a histogram using Plotly Express
            fig2 = px.histogram(df2, x='values', nbins=10, title='Histogram')

            fig2.update_layout(
                plot_bgcolor='white',  # Background color of the plot area
                paper_bgcolor='white'  # Background color of the entire figure
            )

            # Display the histogram in the Streamlit app
            fig2.update_layout(width=1200, height=500)
            st.plotly_chart(fig2)


    with tab2:
        st.text("Aca iran los slicers para filtrar")

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
