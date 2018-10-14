
from sqlalchemy import *
import pandas as pd
import numpy as np


engine = create_engine('postgresql://postgres:Qwe12345@localhost:5432/FRD')
file_name = 'C:\\SeScFRD\\Input\\StoreWithHierarchy.xlsx' 
tableName = "StoreWithHierarchy"

#file_name = 'C:\\SeScFRD\\Input\\ItamarData.xlsx' 
#tableName = "ItamarBaseData"


df = pd.read_excel(file_name)
df.to_sql(con=engine,  name=tableName, if_exists='replace') 