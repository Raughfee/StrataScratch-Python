# Import your libraries
import pandas as pd

# Start writing code
df = employee.copy()
df = df.groupby(['department', 'first_name'])['salary'].sum().reset_index(name = 'salary').sort_values(by = [ 'salary'], ascending = [ False])
df['rank'] = df.groupby('department')['salary'].rank(method = 'dense', ascending = False)
df = df[df['rank'] == 1][['department', 'first_name', 'salary']]
df