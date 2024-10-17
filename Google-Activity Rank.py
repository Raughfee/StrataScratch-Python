# Import your libraries
import pandas as pd

# Start writing code
df = google_gmail_emails.copy()
df = df.groupby('from_user').count().reset_index()
df = df[['from_user', 'id']]
df['rank'] = df['id'].rank(method = 'first', ascending = False)
df = df.sort_values(by = ['rank'], ascending  = True)
df = df.rename(columns = {'id' : 'total_emails'})
df