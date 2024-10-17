# Import your libraries
import pandas as pd

# Start writing code
df = sf_employee.copy()
df1 = sf_bonus.groupby('worker_ref_id')['bonus'].sum().reset_index()
df2 = pd.merge(df, df1, how = 'inner', left_on = 'id', right_on = 'worker_ref_id')
df2 = df2.groupby(['employee_title', 'sex']).agg({'salary': 'mean', 'bonus': 'mean'}).reset_index()
df2['avg_total_comp'] = df2['salary'] + df2['bonus']
df2 = df2[['employee_title', 'sex', 'avg_total_comp']]
df2