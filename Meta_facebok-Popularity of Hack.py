# Import your libraries
import pandas as pd

# Start writing code
df = facebook_employees.copy()
df = pd.merge(df, facebook_hack_survey, how = 'left', left_on = 'id', right_on = 'employee_id')
df = df.groupby('location')['popularity'].mean().reset_index()
df