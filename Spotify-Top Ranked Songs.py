# Import your libraries
import pandas as pd

# Start writing code
df = spotify_worldwide_daily_song_ranking.copy()
df = df[df['position'] == 1].groupby('trackname')['trackname'].count().reset_index(name = 'times_top1').sort_values(by = 'times_top1', ascending = False )
df