# Import your libraries
import pandas as pd

# Start writing code
df = ms_download_facts.copy()
df = pd.merge(df, ms_user_dimension, how = 'left', left_on= 'user_id', right_on = 'user_id')
df1 = pd.merge( df, ms_acc_dimension, how = 'left', on = 'acc_id')
df2 = df1[df1['paying_customer']== 'no'].groupby('date')['downloads'].sum().reset_index()
df3 = df1[df1['paying_customer']== 'yes'].groupby('date')['downloads'].sum().reset_index()
df4 = pd.merge(df2, df3, how = 'left', on = 'date')
df4 = df4[df4['downloads_x'] > df4['downloads_y']]
df4