import psycopg2
from sqlalchemy import *


db = create_engine('postgresql://postgres:Qwe12345@localhost:5432/FRD')
#engine = sa.create_engine('mssql+pymssql://sa:Qwe12345d@WILAF250128-M7Y/Test')


db.echo = False  # Try changing this to True and see what happens

metadata = MetaData(db)

users = Table('users1', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String),
)
users.create()

i = users.insert()
i.execute(name='Mary', age=30, password='secret')
i.execute({'name': 'John', 'age': 42},
          {'name': 'Susan', 'age': 57},
          {'name': 'Carl', 'age': 33})

dict = {'name': 'Jskolm', 'age': 77}

i.execute(dict)

s = users.select()
rs = s.execute()

row = rs.fetchone()
print( 'Id:', row[0])
print ('Name:', row['name'])
print ('Age:', row.age)
print ('Password:', row[users.c.password])

for row in rs:
    print (row.name, 'is', row.age, 'years old')

