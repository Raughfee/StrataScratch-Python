# Import your libraries
import pandas as pd

# Start writing code
df = forbes_global_2010_2014.copy()
df = df.groupby(['company', 'continent'])['profits'].sum().reset_index(name = 'profits').sort_values(by = 'profits', ascending = False)
df['rank'] = df['profits'].rank(method = 'dense', ascending = False)
df = df[df['rank'] == 1]
df = df[['company', 'continent']]
df