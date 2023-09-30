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
                genre1 = st.radio("Dirección hidráulica",["Sin filtro", "Si", "No"])
                genre2 = st.radio("Vidrios eléctricos",["Sin filtro", "Si", "No"])
                genre3 = st.radio("Volante ajustable",["Sin filtro", "Si", "No"])
                genre4 = st.radio("Luces de Xenón/Bixenón",["Sin filtro", "Si", "No"])
                genre5 = st.radio("Sensores frontales",["Sin filtro", "Si", "No"])

                if genre1 != "Sin filtro":
                    filters["Dirección hidráulica"] = genre1
                if genre2 != "Sin filtro":
                    filters["Vidrios eléctricos"] = genre2
                if genre3 != "Sin filtro":
                    filters["Volante ajustable"] = genre3
                if genre4 != "Sin filtro":
                    filters["Luces de Xenón/Bixenón"] = genre4
                if genre5 != "Sin filtro":
                    filters["Sensores frontales"] = genre5

                df = df[df['Dirección hidráulica'] == genre1] if genre1 != 'Sin filtro' else df
                df = df[df['Vidrios eléctricos'] == genre2] if genre2 != 'Sin filtro' else df
                df = df[df['Volante ajustable'] == genre3] if genre3 != 'Sin filtro' else df
                df = df[df['Luces de Xenón/Bixenón'] == genre4] if genre4 != 'Sin filtro' else df
                df = df[df['Sensores frontales'] == genre5] if genre5 != 'Sin filtro' else df

            with colfiltros7:        
                
                genre6 = st.radio("Aros de lujo",["Todo", "Si", "No"])
                genre7 = st.radio("Bluetooth",["Todo", "Si", "No"])
                genre8 = st.radio("Control de radio en el volante",["Todo", "Si", "No"])
                genre9 = st.radio("Asiento con memoria",["Todo", "Si", "No"])
                genre10 = st.radio("Vidrios tintados",["Todo", "Si", "No"])

                if genre6 != "Sin filtro":
                    filters["Aros de lujo"] = genre6
                if genre7 != "Sin filtro":
                    filters["Bluetooth"] = genre7
                if genre8 != "Sin filtro":
                    filters["Control de radio en el volante"] = genre8
                if genre9 != "Sin filtro":
                    filters["Asiento con memoria"] = genre9
                if genre10 != "Sin filtro":
                    filters["Vidrios tintados"] = genre10

                df = df[df['Aros de lujo'] == genre6] if genre6 != 'Sin filtro' else df
                df = df[df['Bluetooth'] == genre7] if genre7 != 'Sin filtro' else df
                df = df[df['Control de radio en el volante'] == genre8] if genre8 != 'Sin filtro' else df
                df = df[df['Asiento con memoria'] == genre9] if genre9 != 'Sin filtro' else df
                df = df[df['Vidrios tintados'] == genre10] if genre10 != 'Sin filtro' else df

            with colfiltros8:
                
                genre11 = st.radio("Tapicería de cuero",["Todo", "Si", "No"])
                genre12 = st.radio("Aire acondicionado climatizado",["Todo", "Si", "No"])
                genre13 = st.radio("Llave inteligente/botón de arranque",["Todo", "Si", "No"])
                genre14 = st.radio("Sensor de lluvia",["Todo", "Si", "No"])
                genre15 = st.radio("Aire acondicionado",["Todo", "Si", "No"])

                if genre11 != "Sin filtro":
                    filters["Tapicería de cuero"] = genre11
                if genre12 != "Sin filtro":
                    filters["Aire acondicionado climatizado"] = genre12
                if genre13 != "Sin filtro":
                    filters["Llave inteligente/botón de arranque"] = genre13
                if genre14 != "Sin filtro":
                    filters["Sensor de lluvia"] = genre14
                if genre15 != "Sin filtro":
                    filters["Aire acondicionado"] = genre15

                df = df[df['Tapicería de cuero'] == genre11] if genre11 != 'Sin filtro' else df
                df = df[df['Aire acondicionado climatizado'] == genre12] if genre12 != 'Sin filtro' else df
                df = df[df['Llave inteligente/botón de arranque'] == genre13] if genre13 != 'Sin filtro' else df
                df = df[df['Sensor de lluvia'] == genre14] if genre14 != 'Sin filtro' else df
                df = df[df['Aire acondicionado'] == genre15] if genre15 != 'Sin filtro' else df

            with colfiltros9:
                
                genre16 = st.radio("Cassette",["Todo", "Si", "No"])
                genre17 = st.radio("Frenos ABS",["Todo", "Si", "No"])
                genre18 = st.radio("Control electrónico de estabilidad",["Todo", "Si", "No"])
                genre19 = st.radio("Monitor de presión de llantas",["Todo", "Si", "No"])
                genre20 = st.radio("Disco compacto",["Todo", "Si", "No"])

                if genre16 != "Sin filtro":
                    filters["Cassette"] = genre16
                if genre17 != "Sin filtro":
                    filters["Frenos ABS"] = genre17
                if genre18 != "Sin filtro":
                    filters["Control electrónico de estabilidad"] = genre18
                if genre19 != "Sin filtro":
                    filters["Monitor de presión de llantas"] = genre19
                if genre20 != "Sin filtro":
                    filters["Disco compacto"] = genre20

                df = df[df['Cassette'] == genre16] if genre16 != 'Sin filtro' else df
                df = df[df['Frenos ABS'] == genre17] if genre17 != 'Sin filtro' else df
                df = df[df['Control electrónico de estabilidad'] == genre18] if genre18 != 'Sin filtro' else df
                df = df[df['Monitor de presión de llantas'] == genre19] if genre19 != 'Sin filtro' else df
                df = df[df['Disco compacto'] == genre20] if genre20 != 'Sin filtro' else df

            with colfiltros10:
                
                genre21 = st.radio("Bolsa de aire",["Todo", "Si", "No"])
                genre22 = st.radio("Sunroof/techo panorámico",["Todo", "Si", "No"])
                genre23 = st.radio("Control de descenso",["Todo", "Si", "No"])
                genre24 = st.radio("Computadora de viaje",["Todo", "Si", "No"])
                genre25 = st.radio("Radio con USB/AUX",["Todo", "Si", "No"])

                if genre21 != "Sin filtro":
                    filters["Bolsa de aire"] = genre21
                if genre22 != "Sin filtro":
                    filters["Sunroof/techo panorámico"] = genre22
                if genre23 != "Sin filtro":
                    filters["Control de descenso"] = genre23
                if genre24 != "Sin filtro":
                    filters["Computadora de viaje"] = genre24
                if genre25 != "Sin filtro":
                    filters["Radio con USB/AUX"] = genre25

                df = df[df['Bolsa de aire'] == genre21] if genre21 != 'Sin filtro' else df
                df = df[df['Sunroof/techo panorámico'] == genre22] if genre22 != 'Sin filtro' else df
                df = df[df['Control de descenso'] == genre23] if genre23 != 'Sin filtro' else df
                df = df[df['Computadora de viaje'] == genre24] if genre24 != 'Sin filtro' else df
                df = df[df['Radio con USB/AUX'] == genre25] if genre25 != 'Sin filtro' else df

            with colfiltros11:
                
                genre26 = st.radio("Alarma",["Todo", "Si", "No"])
                genre27 = st.radio("Cámara de retroceso",["Todo", "Si", "No"])
                genre28 = st.radio("Caja de cambios dual",["Todo", "Si", "No"])
                genre29 = st.radio("Retrovisores auto-retractibles",["Todo", "Si", "No"])
                genre30 = st.radio("Revisión Técnica al día",["Todo", "Si", "No"])

                if genre26 != "Sin filtro":
                    filters["Alarma"] = genre26
                if genre27 != "Sin filtro":
                    filters["Cámara de retroceso"] = genre27
                if genre28 != "Sin filtro":
                    filters["Caja de cambios dual"] = genre28
                if genre29 != "Sin filtro":
                    filters["Retrovisores auto-retractibles"] = genre29
                if genre30 != "Sin filtro":
                    filters["Revisión Técnica al día"] = genre30

                df = df[df['Alarma'] == genre26] if genre26 != 'Sin filtro' else df
                df = df[df['Cámara de retroceso'] == genre27] if genre27 != 'Sin filtro' else df
                df = df[df['Caja de cambios dual'] == genre28] if genre28 != 'Sin filtro' else df
                df = df[df['Retrovisores auto-retractibles'] == genre29] if genre29 != 'Sin filtro' else df
                df = df[df['Revisión Técnica al día'] == genre30] if genre30 != 'Sin filtro' else df

            with colfiltros12:
                
                genre31 = st.radio("Espejos eléctricos",["Todo", "Si", "No"])
                genre32 = st.radio("Desempañador Trasero",["Todo", "Si", "No"])
                genre33 = st.radio("Sensores de retroceso",["Todo", "Si", "No"])
                genre34 = st.radio("Turbo",["Todo", "Si", "No"])
                genre35 = st.radio("Cierre central",["Todo", "Si", "No"])
    
                if genre31 != "Sin filtro":
                    filters["Espejos eléctricos"] = genre31
                if genre32 != "Sin filtro":
                    filters["Desempañador Trasero"] = genre32
                if genre33 != "Sin filtro":
                    filters["Sensores de retroceso"] = genre33
                if genre34 != "Sin filtro":
                    filters["Turbo"] = genre34
                if genre35 != "Sin filtro":
                    filters["Cierre central"] = genre35

                df = df[df['Espejos eléctricos'] == genre31] if genre31 != 'Sin filtro' else df
                df = df[df['Desempañador Trasero'] == genre32] if genre32 != 'Sin filtro' else df
                df = df[df['Sensores de retroceso'] == genre33] if genre33 != 'Sin filtro' else df
                df = df[df['Turbo'] == genre34] if genre34 != 'Sin filtro' else df
                df = df[df['Cierre central'] == genre35] if genre35 != 'Sin filtro' else df

            with colfiltros13:
                
                genre36 = st.radio("Control crucero",["Todo", "Si", "No"])
                genre37 = st.radio("Halógenos",["Todo", "Si", "No"])
                genre38 = st.radio("Volante multifuncional",["Todo", "Si", "No"])
                genre39 = st.radio("Asientos eléctricos",["Todo", "Si", "No"])

                if genre36 != "Sin filtro":
                    filters["Control crucero"] = genre36
                if genre37 != "Sin filtro":
                    filters["Halógenos"] = genre37
                if genre38 != "Sin filtro":
                    filters["Volante multifuncional"] = genre38
                if genre39 != "Sin filtro":
                    filters["Asientos eléctricos"] = genre39


                df = df[df['Control crucero'] == genre36] if genre36 != 'Sin filtro' else df
                df = df[df['Halógenos'] == genre37] if genre37 != 'Sin filtro' else df
                df = df[df['Volante multifuncional'] == genre38] if genre38 != 'Sin filtro' else df
                df = df[df['Asientos eléctricos'] == genre39] if genre39 != 'Sin filtro' else df
        
        for column, value in filters.items():
            filtered_df = filtered_df[filtered_df[column] == value]      
   
        st.write(df)

        st.write(filters)
        
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
