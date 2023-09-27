import streamlit as st
import time
import pandas as pd
import numpy as np
import os
from datetime import datetime, date, time, timedelta, timezone
import pymongo
import pandas as pd
from pandas import json_normalize
import json
import harperdb

from datetime import date
from datetime import datetime
import time


path= "https://raw.githubusercontent.com/jchavesmartinez/StreamlitBudget/main/Budget.csv"
Budget2023 = pd.read_csv(path, encoding='latin-1',index_col=0)

with st.expander("Presupuesto 2023"):
    st.dataframe(Budget2023,use_container_width=True)