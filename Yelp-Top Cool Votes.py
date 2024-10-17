# Import your libraries
import pandas as pd

# Start writing code
df = yelp_reviews.copy()
df = df.groupby(['business_name', 'review_text'])['cool'].sum().reset_index().sort_values(by = ['business_name','cool'], ascending = (False, False))
df['rank'] = df['cool'].rank(method = 'dense', ascending = False)
df = df[df['rank'] == 1][['business_name', 'review_text']]
df