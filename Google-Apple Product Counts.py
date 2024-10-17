# Import your libraries
import pandas as pd

# Start writing code
df = playbook_events.copy()
df = pd.merge(df, playbook_users, how = 'left', on = 'user_id')
df1 = df.groupby(['language'])['user_id'].nunique().reset_index(name = 'n_total_users').sort_values(by = ['n_total_users'], ascending = False)
df2 = df[df['device'].isin(['macbook pro', 'iphone 5s', 'ipad air'])].groupby(['language'])['user_id'].nunique().reset_index(name = 'n_apple_users').sort_values(by = ['n_apple_users'], ascending = False)
df3 = pd.merge( df1, df2, how = 'left', on = 'language')
df3['n_apple_users']  = df3['n_apple_users'].fillna(0)
df3