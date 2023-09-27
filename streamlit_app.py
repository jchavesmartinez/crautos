import streamlit as st
import pandas as pd
import numpy as np
#import harperdb


URL = "https://prueba-arimafintech.harperdbcloud.com"
USERNAME = "ARIMAFINTECH"
PASSWORD = "Jccm130199!"
#db = harperdb.HarperDB(url=URL, username=USERNAME, password=PASSWORD)

#SCHEMA= str('PRESUPUESTO_FAMILIAR')
#TABLE1= str('DIARIO')
#Diario=pd.DataFrame(db.sql("SELECT * FROM {0}.{1}".format(SCHEMA,TABLE1)))


df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)