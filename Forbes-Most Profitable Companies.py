# Import your libraries
import pandas as pd

# Start writing code
df = forbes_global_2010_2014.copy()
df = df.groupby('company')['profits'].sum().reset_index().sort_values(by = 'profits', ascending = False)
df['rank'] = df['profits'].rank(ascending = False)
df = df[df['rank'] <= 3]
df = df[['company', 'profits']]
df