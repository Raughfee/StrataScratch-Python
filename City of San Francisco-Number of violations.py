# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations.copy()
df = df[df['business_name'] == 'Roxanne Cafe']
df['inspection_date'] = pd.to_datetime(df['inspection_date']).dt.year
df = df.groupby('inspection_date')['violation_id'].count().reset_index().sort_values(by = ['inspection_date', 'violation_id'], ascending =[True, False])
df