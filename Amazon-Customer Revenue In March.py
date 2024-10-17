# Import your libraries
import pandas as pd

# Start writing code
df = orders.copy()
df = df[df['order_date'].dt.month == 3].groupby('cust_id')['total_order_cost'].sum().reset_index(name = 'revenue').sort_values(by = 'revenue', ascending = False)
df