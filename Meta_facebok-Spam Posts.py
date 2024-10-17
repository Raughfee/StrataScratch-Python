# Import your libraries
import pandas as pd

# Start writing code
df = facebook_posts.copy()
df = pd.merge(df, facebook_post_views, how = 'inner', on = 'post_id')
df1 = df.groupby('post_date')['post_keywords'].count().reset_index()
df2 = df[df['post_keywords'].str.contains('spam')].groupby('post_date')['post_keywords'].count().reset_index()
df3 = pd.merge(df1,df2, how = 'left', on = 'post_date',  suffixes=('_total','_filtered'))
df3['spam_share'] = df3['post_keywords_filtered']*100/df3['post_keywords_total']
df3= df3[['post_date', 'spam_share']]
df3