# Import your libraries
import pandas as pd

# Start writing code
df = oscar_nominees.copy()
unique_movies_count = df[df['nominee'] == 'Abigail Breslin']['movie'].nunique()