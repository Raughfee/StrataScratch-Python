# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_hosts.copy()
df = pd.merge(df,airbnb_guests, how = 'left', on = 'nationality')
df = df[(df['gender_x']) == df['gender_y']]
df['host_id'] = df['host_id'].drop_duplicates()
df = df[df['host_id'].notnull()]
df = df[['host_id', 'guest_id']]
df