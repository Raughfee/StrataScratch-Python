# Import your libraries
import pandas as pd

# Start writing code
df = facebook_reactions.copy()
df = pd.merge(df, facebook_posts, how = 'left', on = 'post_id')
df = df[df['reaction'] == 'heart']
df = df[['post_id', 'poster_x', 'post_text', 'post_keywords', 'post_date']]
df = df.drop_duplicates()