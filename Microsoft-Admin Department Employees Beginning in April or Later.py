# Import your libraries
import pandas as pd

# Start writing code
df = worker.copy()
df =df[(df['department'] == 'Admin') & (df['joining_date'] >= '2014-04-01')]['worker_id'].count()