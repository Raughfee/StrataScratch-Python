# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business.copy()
df['category'] = df['categories'].str.split(';')
df = df.explode('category')
df = df.groupby('category')['review_count'].sum().reset_index(name = 'total_reviews').sort_values(by = 'total_reviews', ascending = False)
df