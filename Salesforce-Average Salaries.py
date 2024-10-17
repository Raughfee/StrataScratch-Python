# Import your libraries
import pandas as pd

# Start writing code
df = employee.copy()
df['avg_salary'] = df.groupby('department')['salary'].transform('mean')

df = df[['department', 'first_name', 'salary', 'avg_salary']].sort_values(by = 'department', ascending = True)
df