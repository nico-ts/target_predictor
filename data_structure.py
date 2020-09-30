#dependencies
from sqlalchemy import create_engine
import pymysql 
import pandas as pd
import os

#environment variables
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')
db_host = os.environ.get('TS_HOST')

#db connection
db_connection_str = 'mysql+pymysql://' + db_user + ':' + db_password + '@' + db_host + '/TropicSport'
db_connection = create_engine(db_connection_str)

#query
df = pd.read_sql('SELECT target FROM fb_targeting LIMIT 20', con=db_connection)
print(df.head())

#transform
df['target'] = df['target'].map(lambda x: dict(eval(x)))

d = df['target'].apply(pd.Series)
#print(d)

c = d['custom_audiences'].apply(pd.Series)
c.columns = c.columns.astype(str)
c = c.rename(columns=lambda x: x+'_aud') 
#print(c)

b = d['excluded_custom_audiences'].apply(pd.Series)
b.columns = b.columns.astype(str)
b = b.rename(columns=lambda x: x+'_excl') 
#print(b)

a = pd.concat([d, c, b], axis = 1)
print(a)
#a.to_csv('file102.csv')
