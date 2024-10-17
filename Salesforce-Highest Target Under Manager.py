# Import your libraries
import pandas as pd

# Start writing code
df = salesforce_employees.copy()
df = df[df['manager_id'] == 13][['first_name', 'target']]
df['rank'] = df['target'].rank(method =  'dense', ascending = False)
df = df[df['rank'] == 1][['first_name', 'target']]
df