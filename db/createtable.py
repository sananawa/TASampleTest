
#Command: cd db -> python createtable.py
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey

engine = create_engine('sqlite:///touchlessAutomation.db', echo=True)
meta = MetaData()

conn = engine.connect()

users = Table(
   'users', meta, 
   Column('id', Integer, primary_key = True), 
   Column('first_name', String), 
   Column('last_name', String), 
   Column('email_id', String)
)

roles = Table(
   'roles', meta, 
   Column('id', Integer, primary_key = True), 
   Column('user_id', Integer, ForeignKey('users.id')), 
   Column('user_role', String)    
)

meta.create_all(engine)

conn.execute(users.insert(), [
   {'first_name':'sachin', 'last_name':'nanaware' , 'email_id' : 'sachin.nanaware@otis.com'},
   {'first_name':'shubham', 'last_name' : 'reddy', 'email_id' : 'shubham.readdy@otis.com'},
])

conn.execute(roles.insert(), [
   {'user_id':1, 'user_role':'user'},
   {'user_id':1, 'user_role':'admin'},
   {'user_id':2, 'user_role':'user'},
])

#conn.execute("commit")



