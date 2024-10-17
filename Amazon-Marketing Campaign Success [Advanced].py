# Import your libraries
import pandas as pd

# Start writing code
df = marketing_campaign
df = df.drop_duplicates(subset = ['user_id', 'product_id'])

df1 = df.groupby('user_id')['created_at'].min().reset_index()
df2 = df.groupby('user_id')['created_at'].max().reset_index()
df3 = pd.merge(df1,df2, how = 'inner', on = 'user_id')
df4 = df3[df3['created_at_x'] != df3['created_at_y']].reset_index()
df4 = df4['created_at_x'].shape[0]