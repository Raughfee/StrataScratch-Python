# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_hosts.copy()
df = pd.merge(df, airbnb_units, how = 'left', on = 'host_id')
df = df[(df['unit_type'] == 'Apartment') & (df['age'] < 30)]
df = df.groupby('nationality')['unit_id'].nunique().reset_index()
df