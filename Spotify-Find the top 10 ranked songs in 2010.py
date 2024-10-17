# Import your libraries
import pandas as pd

# Start writing code
df = billboard_top_100_year_end.copy()
df = df[(df['year'] == 2010) & (df['year_rank'] <= 10)]
df = df[['year_rank', 'group_name', 'song_name']].drop_duplicates()