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

    st.write(max(df['Kilometraje']))

    tab1, tab2 = st.tabs(["Metricas del mercado", "Potenciales inversiones"])
    
    with tab1:
    
        with st.expander("Menu de filtros"):
            colfiltros1, colfiltros2 = st.columns([1, 1])

            with colfiltros1:
                fechafiltro = st.slider('Año', min(df['Año']), max(df['Año']), (min(df['Año']), max(df['Año'])))
                
            with colfiltros2:
                preciofiltro = st.slider('Precio (Millones)', float(min(df['Precio'])/1000000), float(max(df['Precio'])/1000000), (float(min(df['Precio']))/1000000,float(max(df['Precio']))/1000000), step=500000/1000000)

            preciofiltro = st.slider('Kilometros', int(min(df['Kilometraje'])), int(max(df['Kilometraje'])), (int(min(df['Kilometraje'])),int(max(df['Kilometraje']))), step=10000)


            colfiltros3, colfiltros4, colfiltros5 = st.columns([1, 1,1])

            with colfiltros3:

                marcafiltro = st.selectbox('Marca',tuple(df['Marca'].drop_duplicates().values))
                cilindradafiltro = st.selectbox('Cilindrada',tuple(df['Cilindrada'].drop_duplicates().values))
            
            with colfiltros4:

                modelofiltro = st.selectbox('Modelo',tuple(df['MarcaModelo'].drop_duplicates().values))
                combustionfiltro = st.selectbox('Combustible',tuple(df['Combustible'].drop_duplicates().values))

            
            with colfiltros5:

                estilofiltro = st.selectbox('Estilo',tuple(df['Estilo'].drop_duplicates().values))
                pasajerosfiltro = st.selectbox('Pasajeros',tuple(df['Pasajeros'].drop_duplicates().values))
            
            estadofiltro = st.selectbox('Estado',tuple(df['Estado'].drop_duplicates().values))
            extcolfiltro = st.selectbox('Color exterior',tuple(df['Color ext'].drop_duplicates().values))


            transmisionfiltro = st.selectbox('Transmision',tuple(df['Transmision'].drop_duplicates().values))
            placafiltro = st.selectbox('Placa',tuple(df['Placa'].drop_duplicates().values))
            puertasfiltro = st.selectbox('Puertas',tuple(df['Puertas'].drop_duplicates().values))
            intcolfiltro = st.selectbox('Color interior',tuple(df['Color int'].drop_duplicates().values))


        col1, col2 = st.columns([1, 1])

        with col1:
            # Create a sample DataFrame (replace this with your 'df' from the CSV)
            

            option = st.selectbox(
                'How would you like to be contacted?',
                ('Marca','MarcaModelo','Precio','Cilindrada','Estilo','Pasajeros','Combustible','Transmision','Estado','Kilometraje','Placa','Color ext','Color int','Puertas','Provincia','Grupo de años'))
                        
            
            data1 = {'values': df[option].values}
            df1 = pd.DataFrame(data1)

            # Create a histogram using Plotly Express
            fig1 = px.histogram(df1, x='values', nbins=10, title='Histogram')

            fig1.update_layout(
                plot_bgcolor='white',  # Background color of the plot area
                paper_bgcolor='white'  # Background color of the entire figure
            )

            # Display the histogram in the Streamlit app
            fig1.update_layout(width=760, height=500)
            st.plotly_chart(fig1)

        with col2:
            
            
            option2 = st.selectbox(
                'WENAS',
                ('Marca','MarcaModelo','Precio','Cilindrada','Estilo','Pasajeros','Combustible','Transmision','Estado','Kilometraje','Placa','Color ext','Color int','Puertas','Provincia','Grupo de años'))
            

            # Create a sample DataFrame (replace this with your 'df' from the CSV)
            data2 = {'values': df[option2].values}
            df2 = pd.DataFrame(data2)

            # Create a histogram using Plotly Express
            fig2 = px.histogram(df2, x='values', nbins=10, title='Histogram')

            fig2.update_layout(
                plot_bgcolor='white',  # Background color of the plot area
                paper_bgcolor='white'  # Background color of the entire figure
            )

            # Display the histogram in the Streamlit app
            fig2.update_layout(width=760, height=500)
            st.plotly_chart(fig2)


    with tab2:
        st.text("Wenas")

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
