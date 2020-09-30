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
print(d)
#d.to_csv('file100.csv')

b = d['excluded_custom_audiences'].apply(pd.Series)
print(b)
#b.to_csv('file101.csv')
