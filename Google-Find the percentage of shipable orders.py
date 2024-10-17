# Import your libraries
import pandas as pd

# Start writing code
df = orders.copy()
df = pd.merge(df, customers, how = 'left', left_on = 'cust_id', right_on = 'id')
rows_null = df[df['address'].isnull()].shape[0]
percentages =100 - (rows_null *100/ df.shape[0])
percentages