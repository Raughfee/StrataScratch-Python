# Import your libraries
import pandas as pd

# Start writing code
df = employee.copy()
df1 = pd.merge(df, employee, how = 'left', left_on = 'manager_id', right_on = 'id')
df1 = df1[(df1['salary_x']) > (df1['salary_y'])][['first_name_x', 'salary_x']]
df1