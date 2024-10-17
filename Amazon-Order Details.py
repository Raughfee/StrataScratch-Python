# Import your libraries
import pandas as pd

# Start writing code
df = customers.copy()
df = pd.merge(df, orders, how = 'left', left_on = 'id', right_on = 'cust_id')
df['order_date'] = pd.to_datetime(df['order_date']).dt.date
df = df[df['first_name'].isin(['Jill', 'Eva'])][['first_name', 'order_date','order_details','total_order_cost']]
df