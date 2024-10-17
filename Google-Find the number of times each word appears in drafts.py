# Import your libraries
import pandas as pd

# Start writing code
df = google_file_store.copy()
df = df[df['filename'].str.contains('draft',  case=False, regex=True)]
df = df['contents'].str.split(' ', expand=True)
df = df.stack().reset_index(drop=True).to_frame(name='word')
df['word'] = df['word'].str.strip('.,').str.lower()
df = df.groupby('word').size().reset_index(name='nentry').sort_values(by = ['word', 'nentry'], ascending = [False, False])
df