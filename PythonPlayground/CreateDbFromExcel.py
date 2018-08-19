import psycopg2
from sqlalchemy import *
import pandas as pd
import numpy as np


engine = create_engine('postgresql://postgres:Qwe12345@localhost:5432/FRD')


file_name = 'C:\\SeScFRD\\FinalRescan\\phase3Rescan.xlsx'
df = pd.read_excel(file_name)
df.to_sql(con=engine,  name="phase3Rescan1", if_exists='replace') #df.to_sql(con=engine, index_label='id', name="phase3Rescan1", if_exists='replace')

df1 = pd.read_sql_query('select * from "phase3Rescan1"',con=engine)

dfHead = df1.head(10)
dfHead.to_sql(con=engine,  name="phase3RescanOnlyHead", if_exists='replace')

############################

#add line
metadata = MetaData(engine)

keys = df.columns.tolist()
values = np.arange(df.columns.size).tolist()
dictionary = dict(zip(keys, values))

phase3RescanOnlyHeadTable = Table('phase3RescanOnlyHead', metadata, autoload=True)

insert = phase3RescanOnlyHeadTable.insert()
insert.execute(dictionary)

select = phase3RescanOnlyHeadTable.select()
rs = select.execute()

for row in rs:
    print (row)

print ("succeed")
