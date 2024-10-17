# Import your libraries
import pandas as pd

# Start writing code
df = employee.copy()
df1 = df['salary'].max()
df2 = df[df['salary'] < df1]
df2 = df2['salary'].max()