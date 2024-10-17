# Import your libraries
import pandas as pd
from math import ceil
# Start writing code
df = linkedin_projects.copy()
df = pd.merge(df, linkedin_emp_projects, how = 'inner', left_on = 'id', right_on = 'project_id')
df = pd.merge(df, linkedin_employees, how = 'inner', left_on = 'emp_id', right_on = 'id', suffixes = ['', '_emp'])
df['start_date'] = pd.to_datetime(df['start_date'])
df['end_date'] = pd.to_datetime(df['end_date'])
df['diff'] = (df['end_date'] -df['start_date']).dt.days
df = df.groupby(['title', 'budget', 'diff'])['salary'].sum().reset_index()
df['prorated_expense'] = ((df['diff']* df['salary'])/365).apply(ceil)
df = df[df['budget'] < df['prorated_expense']]
df = df[['title', 'budget', 'prorated_expense']]
df