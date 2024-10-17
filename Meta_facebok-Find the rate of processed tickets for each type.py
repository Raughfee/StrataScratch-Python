# Import your libraries
import pandas as pd

# Start writing code
df = facebook_complaints.copy()
df['case'] = df['processed'].apply(lambda x: 1 if x == True else 0)
df
df = df.groupby('type').agg(processed_rate=('case','mean')).reset_index()
df
