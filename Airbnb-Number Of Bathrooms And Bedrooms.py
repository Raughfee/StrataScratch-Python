# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_search_details.copy()
df = df.groupby(['city', 'property_type']).agg(
               n_bathrooms_avg = ('bathrooms', 'mean'),
               n_bedrooms_avg  = ('bedrooms', 'mean')).reset_index()
df