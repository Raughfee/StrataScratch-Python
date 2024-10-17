# Import your libraries
import pandas as pd

# Start writing code
df = olympics_athletes_events.copy()
df = df.groupby('games')['id'].nunique().reset_index(name = 'athletes_count')
df['rank'] = df['athletes_count'].rank(method = 'first', ascending = False)
df = df[df['rank'] == 1][['games', 'athletes_count']]
df