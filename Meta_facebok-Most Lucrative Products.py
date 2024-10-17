# Import your libraries
import pandas as pd

# Start writing code
df = online_orders.copy()
df['revenue'] = df['units_sold']* df['cost_in_dollars']
df = df.groupby('product_id')['revenue'].sum().reset_index().sort_values(by = 'revenue', ascending = False )
df['rank'] = df['revenue'].rank(method = 'dense', ascending = False)
df = df[df['rank'] <= 5][['product_id', 'revenue']]
df