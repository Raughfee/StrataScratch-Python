# Import your libraries
import pandas as pd

# Start writing code
df = fact_events.copy()
df['month'] =  pd.to_datetime(df['time_id']).dt.month
df = df.groupby(['client_id', 'month'])['user_id'].nunique().reset_index(name = 'user_num')
df