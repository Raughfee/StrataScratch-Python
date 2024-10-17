# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details.copy()
df['word'] = df['amenities'].apply(lambda x: len(x.split(',')))
df = df.groupby('city')['word'].sum().reset_index(name = 'total_word').sort_values(by = 'total_word', ascending = False)

# Filter the cities with the maximum total word count
df = df[df['total_word'] == df['total_word'].max()][['city']]

# Display the result
df