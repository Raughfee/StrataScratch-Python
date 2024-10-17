# Import your libraries
import pandas as pd

# Start writing code

df = facebook_friends.copy()
df1 = df.groupby('user1')['user2'].count().reset_index()
df2 = df.groupby('user2')['user1'].count().reset_index()
df1 = df1.rename(columns ={'user2':'friend'})
df2 = df2.rename(columns ={'user1':'friend'})
df2 = df2.rename(columns ={'user2':'user1'})
df3 = pd.concat([df1,df2], axis = 0 )
df3 = df3.groupby('user1')['friend'].sum().reset_index()
df3['popularity_percentages'] = (df3['friend'] / df3['friend'].count()) * 100
df3 = df3[['user1', 'popularity_percentages']]