# Import your libraries
import pandas as pd

# Start writing code
df = ms_employee_salary.copy()
df = df.groupby(['id','first_name','last_name', 'department_id'])['salary'].max().reset_index()
df