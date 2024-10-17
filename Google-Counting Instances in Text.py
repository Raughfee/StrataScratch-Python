# Import your libraries
import pandas as pd

# Start writing code
df = google_file_store.copy()
df = df['contents'].str.split(' ', expand = True)
df = df.stack().reset_index(drop = True).to_frame(name = 'Word')
df = df[df['Word'].str.contains('bull|bear', case=False, regex=True)].groupby('Word')['Word'].count().reset_index(name = 'nentry').sort_values(by = ['nentry'], ascending= False )
df