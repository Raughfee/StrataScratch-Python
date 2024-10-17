# Import your libraries
import pandas as pd

# Start writing code
df = db_employee.copy()
df = pd.merge(df, db_dept, how = 'left', left_on = 'department_id', right_on = 'id', suffixes = ('', '_new') )
df1 = df[df['department'].isin(['marketing', 'engineering'])].groupby('department')['salary'].max().reset_index()
salary_range = df1['salary'].max() - df1['salary'].min()