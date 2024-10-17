# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business.copy()
df = df.groupby('name')['review_count'].sum().reset_index(name = 'review_count').sort_values(
      by = 'review_count', ascending = False)
df['rank'] = df['review_count'].rank(method = 'dense', ascending = False)  
df = df[df['rank'] <= 5][['name', 'review_count']]
df