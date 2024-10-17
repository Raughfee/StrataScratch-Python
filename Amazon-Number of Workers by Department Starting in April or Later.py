# Import your libraries
import pandas as pd

# Start writing code
df = worker.copy()
#df['joining_date'] = pd.to_datetime(df['joining_date']).dt.date
df = df[df['joining_date'] >= '2014-04-01'].groupby('department')['worker_id'].count().reset_index(name = 'total_workers').sort_values(by = 'total_workers', ascending = False)
df