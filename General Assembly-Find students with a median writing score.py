# Import your libraries
import pandas as pd
from statistics import median 

# Start writing code
df = sat_scores.copy()
df1 = df['sat_writing'].median()
df = df[df['sat_writing'] == df1]
df = df[['student_id']]