# Import your libraries
import pandas as pd

# Start writing code
df = facebook_web_log.copy()
df['date'] = pd.to_datetime(df['timestamp']).dt.date 
df1 =  df.groupby(['user_id', 'date', 'action'])['timestamp'].max().reset_index()
df1 = df1[df1['action'] == 'page_load']
df2 =  df.groupby(['user_id', 'date', 'action'])['timestamp'].min().reset_index()
df2 = df2[df2['action'] == 'page_exit']
df3 = pd.merge(df1, df2, how = 'left', on = 'user_id')
df3 = df3[df3['date_x'] == df3['date_y']]
df3 = df3[df3['timestamp_x'] < df3['timestamp_y']]
df3['duration'] = df3['timestamp_y'] - df3['timestamp_x']
df3 = df3.groupby('user_id')['duration'].mean().reset_index()
df3