# Import your libraries
import pandas as pd

# Start writing code
df = fb_active_users.copy()
df = df[df['country'] == "USA"].groupby('status')['user_id'].count().to_frame('user_count')
df = df.loc['open'] / df['user_count'].sum()