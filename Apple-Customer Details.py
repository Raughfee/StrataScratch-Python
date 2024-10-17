# Import your libraries
import pandas as pd

# Start writing code
df = customers.copy()
df = pd.merge(df, orders, how = 'left', left_on = 'id', right_on = 'cust_id')
df = df[['first_name', 'last_name', 'city', 'order_details']].sort_values(by= ['first_name', 'order_details'], ascending =[True, True])
df