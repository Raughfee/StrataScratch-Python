# Import your libraries
import pandas as pd

# Start writing code
df = customers.copy()
df = pd.merge( df, orders, how = 'left', left_on = 'id', right_on = 'cust_id')

df = df[(df['order_date'] >= '2019-02-01') & (df['order_date'] <= '2019-05-01') ]
df['order_date'] = pd.to_datetime( df['order_date']).dt.date
df = df.groupby(['first_name', 'order_date'])['total_order_cost'].sum().reset_index().sort_values(by = 'total_order_cost', ascending = False)
df['rank'] = df['total_order_cost'].rank(method = 'dense', ascending = False)
df = df[df['rank'] == 1][['first_name', 'order_date', 'total_order_cost']]