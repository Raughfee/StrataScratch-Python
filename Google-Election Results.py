# Import your libraries
import pandas as pd

# Start writing code
df = voting_results.copy()
df = df[df['candidate'].notnull()]
df['vote_value'] = df.groupby('voter')['voter'].transform('count')
df['vote_value'] = 1/ df['vote_value']
df = df.groupby('candidate')['vote_value'].sum().reset_index()
df['rank'] = df['vote_value'].rank(method = 'dense', ascending = False)
df = df[df['rank'] == 1]['candidate']
df