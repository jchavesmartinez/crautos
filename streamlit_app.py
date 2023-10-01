import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
import time
from streamlit import runtime
from streamlit_dynamic_filters import DynamicFilters


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
    
        filters = {}
        filtered_df = df.copy()


        
        with st.expander("Menu de filtros"):

            dynamic_filters = DynamicFilters(df, filters=['Marca','Cilindrada', 'Estado','Transmision','MarcaModelo','Combustible', 'Color ext','Placa','Estilo','Pasajeros', 'Color int','Puertas'])
            dynamic_filters.display_filters(location='columns', num_columns=2)


            df=dynamic_filters.filter_df()

            st.markdown('<hr>', unsafe_allow_html=True)

            try:

                fechafiltro = st.slider('Año PENDIENTE', min(df['Año']), max(df['Año']), (min(df['Año']), max(df['Año'])), step=1)
                df=df[(df['Año'] >= list(fechafiltro)[0] ) & (df['Año'] < list(fechafiltro)[1])]
            
            except:
                st.write('Solo existe un elemento, no es posible filtrar más los años')

            try:
            
                preciofiltro = st.slider('Precio (Millones) PENDIENTE', float(min(df['Precio'])/1000000), float(max(df['Precio'])/1000000), (float(min(df['Precio']))/1000000,float(max(df['Precio']))/1000000), step=500000/1000000)
                df=df[(df['Precio'] >= list(preciofiltro)[0]*1000000 ) & (df['Precio'] < list(preciofiltro)[1]*1000000)]
    
            except:
                st.write('Solo existe un elemento, no es posible filtrar más el precio')
                
            try:
            
                kmfiltro = st.slider('Kilometros PENDIENTE', int(min(df['Kilometraje'])), int(max(df['Kilometraje'])), (int(min(df['Kilometraje'])),int(max(df['Kilometraje']))), step=10000)
                df=df[(df['Kilometraje'] >= list(kmfiltro)[0] ) & (df['Kilometraje'] < list(kmfiltro)[1])]

            except:
                st.write('Solo existe un elemento, no es posible filtrar más el kilometraje')



    with tab2:

        st.write('wenas')
        # data = {
        #     'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
        #     'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
        #     'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing']
        #     }

        # df = pd.DataFrame(data)

        # dynamic_filters = DynamicFilters(df, filters=['Region', 'Country', 'City'])

        # dynamic_filters.display_filters(location='columns', num_columns=2)

        # dynamic_filters.display_df()



except Exception as e:
    st.error(f"An error occurred: {str(e)}")
