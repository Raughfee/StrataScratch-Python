# Import your libraries
import pandas as pd

# Start writing code
df =  spotify_worldwide_daily_song_ranking.copy()
df = df.groupby('artist')['artist'].count().reset_index(name = 'n_occurence').sort_values(by = 'n_occurence', ascending = False)
df