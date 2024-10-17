# Import your libraries
import pandas as pd

# Start writing code
df = worker.copy()
df = pd.merge(df, title, how = 'left', left_on = 'worker_id', right_on = 'worker_ref_id')
df = df.groupby('worker_title')['salary'].max().reset_index()
df['rank'] = df['salary'].rank(method = 'dense', ascending = False)
df = df[df['rank'] == 1][['worker_title']].rename(columns = {'worker_title': 'best_paid_title'})
df