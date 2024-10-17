# Import your libraries
import pandas as pd

# Start writing code
df = fb_eu_energy.copy()
df = pd.concat([df, fb_asia_energy], axis = 0 )
df = pd.concat([df, fb_na_energy], axis = 0)
df['date'] = pd.to_datetime(df['date']).dt.date
df = df.groupby('date')['consumption'].sum().reset_index().sort_values(by = 'consumption', ascending = False )
df['rank'] = df['consumption'].rank(method = 'dense', ascending = False )
df= df[df['rank'] == 1][['date', 'consumption']]
df