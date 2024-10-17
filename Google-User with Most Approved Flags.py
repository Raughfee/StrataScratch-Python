# Import your libraries
import pandas as pd

# Start writing code
df = user_flags.copy()
df = pd.merge( df, flag_review, how  = 'inner', on = 'flag_id')
df['username'] = df['user_firstname'] + ' ' + df['user_lastname']
df = df[df['reviewed_outcome']== 'APPROVED']
df = df.groupby('username')['video_id'].nunique().reset_index()
df['rank'] = df['video_id'].rank(method = 'dense', ascending  = False)
df = df[df['rank'] == 1]['username']