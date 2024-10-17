# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = amazon_transactions.copy()

df['created_at'] =  pd.to_datetime(df['created_at']).dt.date
df = df.groupby(['user_id','created_at', 'revenue'])['item'].count().reset_index().sort_values(by = ['user_id','created_at'], ascending = [True, False])
df['lag'] = df.groupby('user_id')['created_at'].shift(1)
df
df['days'] = (df['lag'] - df['created_at'])// np.timedelta64(1, 'D')
df = df[(df['days'] <= 7) & (df['days'] >= 0)]
df = df['user_id'].unique()
df