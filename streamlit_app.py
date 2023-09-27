import streamlit as st
import pandas as pd
import numpy as np
import harperdb


URL = "https://prueba-arimafintech.harperdbcloud.com"
USERNAME = "ARIMAFINTECH"
PASSWORD = "Jccm130199!"
db = harperdb.HarperDB(url=URL, username=USERNAME, password=PASSWORD)

SCHEMA= str('CRAUTOS')
TABLE1= str('carros')
Diario=pd.DataFrame(db.sql("SELECT * FROM {0}.{1}".format(SCHEMA,TABLE1)))

print(Diario)

st.dataframe(Diario)