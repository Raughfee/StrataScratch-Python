# Import your libraries
import pandas as pd

# Start writing code
df = sf_transactions.copy()
df['year_month'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m')
df = df.groupby('year_month')['value'].sum().reset_index()
df['diff'] = df['value'].shift(1)
df['revenue_diff_pct'] = ((df['value'] - df['diff'])*100/ df['diff']).round(2)
df = df[['year_month', 'revenue_diff_pct']]