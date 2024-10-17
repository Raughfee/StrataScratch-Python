# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_host_searches.copy()
def calculate_popularity(num_reviews):
    if num_reviews == 0:
        return 'New'
    elif 1 <= num_reviews <= 5:
        return 'Rising'
    elif 6 <= num_reviews <= 15:
        return 'Trending Up'
    elif 16 <= num_reviews <= 40:
        return 'Popular'
    else:
        return 'Hot'
        
df = df.drop_duplicates(subset=['price', 'room_type', 'host_since', 'zipcode', 'number_of_reviews'])       
df['host_popularity'] = df['number_of_reviews'].apply(calculate_popularity) 
df = df.groupby('host_popularity').agg(
                min_price = ('price', 'min'),
                avg_price = ('price', 'mean'),
                max_price = ('price', 'max')).reset_index()
df