# Import your libraries
import pandas as pd

# Start writing code
df = user_flags.copy()
df = df[df['flag_id'].notnull()]
df['username'] = df['user_firstname'].astype(str)+ ' '+ df['user_lastname'].astype(str)
df = df.groupby('video_id')['username'].nunique().reset_index()