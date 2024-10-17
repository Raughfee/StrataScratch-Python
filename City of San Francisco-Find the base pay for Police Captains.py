# Import your libraries
import pandas as pd

# Start writing code
df = sf_public_salaries.copy()
df = df[df['jobtitle'] == 'CAPTAIN III (POLICE DEPARTMENT)'][['employeename','basepay']]