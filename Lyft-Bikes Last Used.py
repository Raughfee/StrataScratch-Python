# Import your libraries
import pandas as pd

# Start writing code
df = dc_bikeshare_q1_2012.copy()
df = df.groupby('bike_number')['end_time'].max().reset_index().sort_values( by = ['end_time'], ascending = False)
df