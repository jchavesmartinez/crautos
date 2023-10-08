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
        df['Kilometraje'] = df['Kilometraje'].fillna(1)
        return df

    # Load the data using the cached function
    df = load_data()

    modelo=df.copy()

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

                fechafiltro = st.slider('Año', min(df['Año']), max(df['Año'])+1, (min(df['Año']), max(df['Año'])+1))
                df=df[(df['Año'] >= list(fechafiltro)[0] ) & (df['Año'] <= list(fechafiltro)[1])]

            except:
                st.write('Solo existe un elemento, no es posible filtrar más los años')

            try:
            
                preciofiltro = st.slider('Precio (Millones)', float(min(df['Precio'])/1000000), float((max(df['Precio'])+1)/1000000), (float(min(df['Precio']))/1000000,float(max(df['Precio'])+1)/1000000), step=500000/1000000)
                df=df[(df['Precio'] >= list(preciofiltro)[0]*1000000 ) & (df['Precio'] <= list(preciofiltro)[1]*1000000)]

            except:
                st.write('Solo existe un elemento, no es posible filtrar más el precio')
                
            try:
            
                kmfiltro = st.slider('Kilometros', int(min(df['Kilometraje'])), int(max(df['Kilometraje']))+1, (int(min(df['Kilometraje'])),int(max(df['Kilometraje']))+1), step=10000)
                df=df[(df['Kilometraje'] >= list(kmfiltro)[0]) & (df['Kilometraje'] <= list(kmfiltro)[1])]
            except:
                st.write('Solo existe un elemento, no es posible filtrar más el kilometraje')

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
                
                genre6 = st.radio("Aros de lujo",["Sin filtro", "Si", "No"])
                genre7 = st.radio("Bluetooth",["Sin filtro", "Si", "No"])
                genre8 = st.radio("Control de radio en el volante",["Sin filtro", "Si", "No"])
                genre9 = st.radio("Asiento con memoria",["Sin filtro", "Si", "No"])
                genre10 = st.radio("Vidrios tintados",["Sin filtro", "Si", "No"])

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
                
                genre11 = st.radio("Tapicería de cuero",["Sin filtro", "Si", "No"])
                genre12 = st.radio("Aire acondicionado climatizado",["Sin filtro", "Si", "No"])
                genre13 = st.radio("Llave inteligente/botón de arranque",["Sin filtro", "Si", "No"])
                genre14 = st.radio("Sensor de lluvia",["Sin filtro", "Si", "No"])
                genre15 = st.radio("Aire acondicionado",["Sin filtro", "Si", "No"])

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
                
                genre16 = st.radio("Cassette",["Sin filtro", "Si", "No"])
                genre17 = st.radio("Frenos ABS",["Sin filtro", "Si", "No"])
                genre18 = st.radio("Control electrónico de estabilidad",["Sin filtro", "Si", "No"])
                genre19 = st.radio("Monitor de presión de llantas",["Sin filtro", "Si", "No"])
                genre20 = st.radio("Disco compacto",["Sin filtro", "Si", "No"])

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
                
                genre21 = st.radio("Bolsa de aire",["Sin filtro", "Si", "No"])
                genre22 = st.radio("Sunroof/techo panorámico",["Sin filtro", "Si", "No"])
                genre23 = st.radio("Control de descenso",["Sin filtro", "Si", "No"])
                genre24 = st.radio("Computadora de viaje",["Sin filtro", "Si", "No"])
                genre25 = st.radio("Radio con USB/AUX",["Sin filtro", "Si", "No"])

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
                
                genre26 = st.radio("Alarma",["Sin filtro", "Si", "No"])
                genre27 = st.radio("Cámara de retroceso",["Sin filtro", "Si", "No"])
                genre28 = st.radio("Caja de cambios dual",["Sin filtro", "Si", "No"])
                genre29 = st.radio("Retrovisores auto-retractibles",["Sin filtro", "Si", "No"])
                genre30 = st.radio("Revisión Técnica al día",["Sin filtro", "Si", "No"])

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
                
                genre31 = st.radio("Espejos eléctricos",["Sin filtro", "Si", "No"])
                genre32 = st.radio("Desempañador Trasero",["Sin filtro", "Si", "No"])
                genre33 = st.radio("Sensores de retroceso",["Sin filtro", "Si", "No"])
                genre34 = st.radio("Turbo",["Sin filtro", "Si", "No"])
                genre35 = st.radio("Cierre central",["Sin filtro", "Si", "No"])
    
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
                
                genre36 = st.radio("Control crucero",["Sin filtro", "Si", "No"])
                genre37 = st.radio("Halógenos",["Sin filtro", "Si", "No"])
                genre38 = st.radio("Volante multifuncional",["Sin filtro", "Si", "No"])
                genre39 = st.radio("Asientos eléctricos",["Sin filtro", "Si", "No"])

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
                
        with st.expander('Estadisticas'):

            for column, value in filters.items():
                df = filtered_df[filtered_df[column] == value]      


            
            col3, col4, col5, col6, col7 , col8, col9 = st.columns(7)
            col3.metric("Carros totales", len(df['Marca']))
            col4.metric("Precio min", int(min(df['Precio'])))
            col5.metric("Precio promedio", int(df['Precio'].mean()))
            col6.metric("Precio moda", int(df['Precio'].mode()))
            col7.metric("Mediana precio", int(df['Precio'].median()))
            col8.metric("Precio maximo", int(max(df['Precio'])))
            col9.metric("Desviacion estandar relativa", str(int((df['Precio'].std()/df['Precio'].mean())*100))+"%")
        
            st.markdown('<hr>', unsafe_allow_html=True)


            col1, col2 = st.columns([1, 1])

            with col1:

                grafico1 = st.radio(
                    "Grafico a mostrar ",
                    ["Histograma", "Dispersión"],
                    horizontal=True,
                )

                st.markdown('<hr>', unsafe_allow_html=True)


                if grafico1=='Histograma':

                    option1 = st.selectbox(
                        'Variable a graficar',
                        ('Grupo de años','MarcaModelo','Marca','Precio','Cilindrada','Estilo','Pasajeros','Combustible','Transmision','Estado','Kilometraje','Placa','Color ext','Color int','Puertas','Provincia'))

                    # Create a sample DataFrame (replace this with your 'df' from the CSV)
                    data1 = {'values': df[option1].values}
                    df1 = pd.DataFrame(data1)

                    # Create a histogram using Plotly Express
                    fig1 = px.histogram(df1, x='values', nbins=10, title='Histograma '+str(option1))

                    fig1.update_layout(
                        plot_bgcolor='white',  # Background color of the plot area
                        paper_bgcolor='white'  # Background color of the entire figure
                    )
                    
                    # Display the histogram in the Streamlit app
                    fig1.update_layout(width=760, height=500)

                    st.plotly_chart(fig1)

                if grafico1=='Dispersión':

                    # Sample data
                    np.random.seed(40)
                    data = pd.DataFrame({
                        'X': np.random.rand(40),
                        'Y': np.random.rand(40),
                        'Category': np.random.choice(['A', 'B'], size=50)
                    })

                    # Scatter plot using Plotly Express
                    fig4 = px.scatter(data, x='X', y='Y', color='Category', title='Aun en desarrollo')

                    fig4.update_layout(width=760, height=500)

                    fig4.update_layout(
                        plot_bgcolor='white',  # Background color of the plot area
                        paper_bgcolor='white'  # Background color of the entire figure
                    )

                    st.plotly_chart(fig4)

            with col2:
                
                
                grafico2 = st.radio(
                    "Grafico a mostrar",
                    ["Histograma", "Dispersión"],
                    horizontal=True,
                )

                st.markdown('<hr>', unsafe_allow_html=True)


                if grafico2=='Histograma':

                    option2 = st.selectbox(
                        'WENAS',
                        ('MarcaModelo','Marca','Precio','Cilindrada','Estilo','Pasajeros','Combustible','Transmision','Estado','Kilometraje','Placa','Color ext','Color int','Puertas','Provincia','Grupo de años'))

                    

                    # Create a sample DataFrame (replace this with your 'df' from the CSV)
                    data2 = {'values': df[option2].values}
                    df2 = pd.DataFrame(data2)

                    # Create a histogram using Plotly Express
                    fig2 = px.histogram(df2, x='values', nbins=10, title='Histograma '+str(option2))

                    fig2.update_layout(
                        plot_bgcolor='white',  # Background color of the plot area
                        paper_bgcolor='white'  # Background color of the entire figure
                    )
                    
                    # Display the histogram in the Streamlit app
                    fig2.update_layout(width=760, height=500)

                    st.plotly_chart(fig2)

                if grafico2=='Dispersión':

                    # Sample data
                    np.random.seed(42)
                    data = pd.DataFrame({
                        'X': np.random.rand(50),
                        'Y': np.random.rand(50),
                        'Category': np.random.choice(['A', 'B'], size=50)
                    })

                    # Scatter plot using Plotly Express
                    fig3 = px.scatter(data, x='X', y='Y', color='Category', title='Aun en desarrollo')

                    fig3.update_layout(width=760, height=500)


                    fig3.update_layout(
                        plot_bgcolor='white',  # Background color of the plot area
                        paper_bgcolor='white'  # Background color of the entire figure
                    )

                    st.plotly_chart(fig3)
                
    with tab2:

        modelo_completo=modelo
        modelo_completo["grupo_id"] = modelo_completo["Marca"].astype(str) + modelo_completo["MarcaModelo"].astype(str) + modelo_completo["Grupo de años"].astype(str)
        st.write(modelo_completo)
        st.write(len(modelo_completo))

        modelo = df.groupby(['Marca', 'MarcaModelo', 'Grupo de años']).agg({'Año': 'mean','Kilometraje':['mean','median'], 'Precio': ['mean', 'count','median','std']}).reset_index()
        modelo.columns = ['Marca', 'MarcaModelo', 'Grupo de años', 'Año_mean','KM_mean','KM_median', 'Precio_mean', 'Precio_count', 'Precio_median','Precio_std']
        modelo['Precio_relativestd']=modelo['Precio_std']/modelo['Precio_mean']*100
        modelo = modelo[modelo['Precio_count'] >= 5]
        modelo["grupo_id"] = modelo["Marca"].astype(str) + modelo["MarcaModelo"].astype(str) + modelo["Grupo de años"].astype(str)

        st.write(modelo)
        st.write(len(modelo))

                # Assuming df1 and df2 are your two DataFrames, and 'common_column' is the column you want to use for merging.
        modelo = pd.merge(modelo_completo, modelo, on='grupo_id', suffixes=('_modelo_completo', '_modelo'))

        # Drop duplicate columns
        modelo = modelo.loc[:, ~modelo.columns.duplicated()]
        modelo['precio_margen_mean']=modelo['Precio']/modelo['Precio_mean']
        modelo['precio_margen_median']=modelo['Precio']/modelo['Precio_median']

        modelo = modelo[modelo['precio_margen_mean'] < 1]
        modelo = modelo[modelo['precio_margen_median'] < 1]

        modelo['precio_margen_mean']=modelo['Precio_mean']-modelo['Precio']
        modelo['precio_margen_median']=modelo['Precio_median']-modelo['Precio']

        modelo = modelo[modelo['precio_margen_mean'] >= 500000]
        modelo = modelo[modelo['precio_margen_median'] >= 500000]

        modelo['km_margen_mean']=modelo['Kilometraje']/modelo['KM_mean']
        modelo['km_margen_median']=modelo['Kilometraje']/modelo['KM_mean']

        modelo = modelo[modelo['km_margen_mean'] <= 0.8]
        modelo = modelo[modelo['km_margen_median'] <= 0.8]
        modelo = modelo[modelo['km_margen_mean'] > 0]

        st.write(modelo)
        st.write(len(modelo))





except Exception as e:
    st.error(f"An error occurred: {str(e)}")
