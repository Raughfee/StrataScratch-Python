# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business.copy()
df = df[df['stars'] == 5].groupby('state')['business_id'].count().reset_index(name = 'n_business').sort_values(by = ['n_business', 'state'], ascending = (False, True))
df['rank'] = df['n_business'].rank(method = 'min', ascending = False)
df = df[df['rank'] <= 5][['state', 'n_business']]
df