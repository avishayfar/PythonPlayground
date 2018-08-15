import psycopg2
from sqlalchemy import *
import pandas as pd


engine = create_engine('postgresql://postgres:Qwe12345@localhost:5432/FRD')

file_name = 'C:\\SeScFRD\\FinalRescan\\phase3Rescan.xlsx'
df = pd.read_excel(file_name)
df.to_sql(con=engine, index_label='id', name="phase3Rescan1", if_exists='replace')

print ("succeed")
