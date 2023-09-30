import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
import time


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
            colfiltros1, colfiltros2 = st.columns([1, 1])

            with colfiltros1:
                fechafiltro = st.slider('Año', min(df['Año']), max(df['Año']), (min(df['Año']), max(df['Año'])))
                
            with colfiltros2:
                preciofiltro = st.slider('Precio (Millones)', float(min(df['Precio'])/1000000), float(max(df['Precio'])/1000000), (float(min(df['Precio']))/1000000,float(max(df['Precio']))/1000000), step=500000/1000000)

            preciofiltro = st.slider('Kilometros', int(min(df['Kilometraje'])), int(max(df['Kilometraje'])), (int(min(df['Kilometraje'])),int(max(df['Kilometraje']))), step=10000)

            st.markdown('<hr>', unsafe_allow_html=True)

            colfiltros3, colfiltros4, colfiltros5 = st.columns([1, 1, 1])

            with colfiltros3:
                
                marcafiltro = st.selectbox('Marca',('Sin filtro',)+tuple(df['Marca'].drop_duplicates().values))
                cilindradafiltro = st.selectbox('Cilindrada',('Sin filtro',)+tuple(df['Cilindrada'].drop_duplicates().values))
                estadofiltro = st.selectbox('Estado',('Sin filtro',)+tuple(df['Estado'].drop_duplicates().values))
                transmisionfiltro = st.selectbox('Transmision',('Sin filtro',)+tuple(df['Transmision'].drop_duplicates().values))
                
                if marcafiltro != "Sin filtro":
                    filters["Marca"] = marcafiltro
                if cilindradafiltro != "Sin filtro":
                    filters["Cilindrada"] = cilindradafiltro
                if estadofiltro != "Sin filtro":
                    filters["Estado"] = estadofiltro
                if transmisionfiltro != "Sin filtro":
                    filters["Transmision"] = transmisionfiltro
                
                df = df[df['Marca'] == marcafiltro] if marcafiltro != 'Sin filtro' else df
                df = df[df['Cilindrada'] == cilindradafiltro] if cilindradafiltro != 'Sin filtro' else df
                df = df[df['Estado'] == estadofiltro] if estadofiltro != 'Sin filtro' else df
                df = df[df['Transmision'] == transmisionfiltro] if transmisionfiltro != 'Sin filtro' else df

            with colfiltros4:

                modelofiltro = st.selectbox('Modelo',('Sin filtro',)+tuple(df['MarcaModelo'].drop_duplicates().values))
                combustionfiltro = st.selectbox('Combustible',('Sin filtro',)+tuple(df['Combustible'].drop_duplicates().values))
                extcolfiltro = st.selectbox('Color exterior',('Sin filtro',)+tuple(df['Color ext'].drop_duplicates().values))
                placafiltro = st.selectbox('Placa',('Sin filtro',)+tuple(df['Placa'].drop_duplicates().values))

                if modelofiltro != "Sin filtro":
                    filters["MarcaModelo"] = modelofiltro
                if combustionfiltro != "Sin filtro":
                    filters["Combustible"] = combustionfiltro
                if extcolfiltro != "Sin filtro":
                    filters["Color ext"] = extcolfiltro
                if placafiltro != "Sin filtro":
                    filters["Placa"] = placafiltro
                
                df = df[df['MarcaModelo'] == modelofiltro] if modelofiltro != 'Sin filtro' else df
                df = df[df['Combustible'] == combustionfiltro] if combustionfiltro != 'Sin filtro' else df
                df = df[df['Color ext'] == extcolfiltro] if extcolfiltro != 'Sin filtro' else df
                df = df[df['Placa'] == placafiltro] if placafiltro != 'Sin filtro' else df

            with colfiltros5:

                estilofiltro = st.selectbox('Estilo',('Sin filtro',)+tuple(df['Estilo'].drop_duplicates().values))
                pasajerosfiltro = st.selectbox('Pasajeros',('Sin filtro',)+tuple(df['Pasajeros'].drop_duplicates().values))
                intcolfiltro = st.selectbox('Color interior',('Sin filtro',)+tuple(df['Color int'].drop_duplicates().values))
                puertasfiltro = st.selectbox('Puertas',('Sin filtro',)+tuple(df['Puertas'].drop_duplicates().values))

                if estilofiltro != "Sin filtro":
                    filters["Estilo"] = estilofiltro
                if pasajerosfiltro != "Sin filtro":
                    filters["Pasajeros"] = pasajerosfiltro
                if intcolfiltro != "Sin filtro":
                    filters["Color int"] = intcolfiltro
                if puertasfiltro != "Sin filtro":
                    filters["Puertas"] = puertasfiltro


                df = df[df['Estilo'] == estilofiltro] if estilofiltro != 'Sin filtro' else df
                df = df[df['Pasajeros'] == pasajerosfiltro] if pasajerosfiltro != 'Sin filtro' else df
                df = df[df['Color int'] == intcolfiltro] if intcolfiltro != 'Sin filtro' else df
                df = df[df['Puertas'] == puertasfiltro] if puertasfiltro != 'Sin filtro' else df


        with st.expander("Extras"):

            colfiltros6, colfiltros7, colfiltros8 , colfiltros9, colfiltros10, colfiltros11, colfiltros12, colfiltros13 = st.columns([1, 1, 1, 1, 1, 1 , 1, 1])

            with colfiltros6:
                genre1 = st.radio("Dirección hidráulica",["Todo", "Si", "No"])
                genre2 = st.radio("Vidrios eléctricos",["Todo", "Si", "No"])
                genre3 = st.radio("Volante ajustable",["Todo", "Si", "No"])
                genre4 = st.radio("Luces de Xenón/Bixenón",["Todo", "Si", "No"])
                genre5 = st.radio("Sensores frontales",["Todo", "Si", "No"])

                st.write(genre)
    
            with colfiltros7:
                genre5 = st.radio("Vidrios tintados",["Todo", "Si", "No"])
                genre6 = st.radio("Aros de lujo",["Todo", "Si", "No"])
                genre7 = st.radio("Bluetooth",["Todo", "Si", "No"])
                genre8 = st.radio("Control de radio en el volante",["Todo", "Si", "No"])
                genre9 = st.radio("Asiento con memoria",["Todo", "Si", "No"])

            with colfiltros8:
                genre10 = st.radio("Aire acondicionado",["Todo", "Si", "No"])
                genre11 = st.radio("Tapicería de cuero",["Todo", "Si", "No"])
                genre12 = st.radio("Aire acondicionado climatizado",["Todo", "Si", "No"])
                genre13 = st.radio("Llave inteligente/botón de arranque",["Todo", "Si", "No"])
                genre14 = st.radio("Sensor de lluvia",["Todo", "Si", "No"])

            with colfiltros9:
                genre15 = st.radio("Disco compacto",["Todo", "Si", "No"])
                genre16 = st.radio("Cassette",["Todo", "Si", "No"])
                genre17 = st.radio("Frenos ABS",["Todo", "Si", "No"])
                genre18 = st.radio("Control electrónico de estabilidad",["Todo", "Si", "No"])
                genre19 = st.radio("Monitor de presión de llantas",["Todo", "Si", "No"])

            with colfiltros10:
                genre20 = st.radio("Radio con USB/AUX",["Todo", "Si", "No"])
                genre21 = st.radio("Bolsa de aire",["Todo", "Si", "No"])
                genre22 = st.radio("Sunroof/techo panorámico",["Todo", "Si", "No"])
                genre23 = st.radio("Control de descenso",["Todo", "Si", "No"])
                genre24 = st.radio("Computadora de viaje",["Todo", "Si", "No"])

            with colfiltros11:
                genre25 = st.radio("Revisión Técnica al día",["Todo", "Si", "No"])
                genre26 = st.radio("Alarma",["Todo", "Si", "No"])
                genre27 = st.radio("Cámara de retroceso",["Todo", "Si", "No"])
                genre28 = st.radio("Caja de cambios dual",["Todo", "Si", "No"])
                genre29 = st.radio("Retrovisores auto-retractibles",["Todo", "Si", "No"])

            with colfiltros12:
                genre30 = st.radio("Cierre central",["Todo", "Si", "No"])
                genre31 = st.radio("Espejos eléctricos",["Todo", "Si", "No"])
                genre32 = st.radio("Desempañador Trasero",["Todo", "Si", "No"])
                genre33 = st.radio("Sensores de retroceso",["Todo", "Si", "No"])
                genre34 = st.radio("Turbo",["Todo", "Si", "No"])

            with colfiltros13:
                genre35 = st.radio("Asientos eléctricos",["Todo", "Si", "No"])
                genre36 = st.radio("Control crucero",["Todo", "Si", "No"])
                genre37 = st.radio("Halógenos",["Todo", "Si", "No"])
                genre38 = st.radio("Volante multifuncional",["Todo", "Si", "No"])

        
        
        for column, value in filters.items():
            filtered_df = filtered_df[filtered_df[column] == value]      
   
        col1, col2 = st.columns([1, 1])

        with col1:
            # Create a sample DataFrame (replace this with your 'df' from the CSV)
            

            option = st.selectbox(
                'How would you like to be contacted?',
                ('Marca','MarcaModelo','Precio','Cilindrada','Estilo','Pasajeros','Combustible','Transmision','Estado','Kilometraje','Placa','Color ext','Color int','Puertas','Provincia','Grupo de años'))
                               
            data1 = {'values': filtered_df[option].values}
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
            data2 = {'values': filtered_df[option2].values}
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

        st.write(len(filtered_df))

    with tab2:

        st.write('wenas')


except Exception as e:
    st.error(f"An error occurred: {str(e)}")
