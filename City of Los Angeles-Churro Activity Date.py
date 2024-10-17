# Import your libraries
import pandas as pd

# Start writing code
df = los_angeles_restaurant_health_inspections.copy()
df['activity_date'] = pd.to_datetime(df['activity_date']).dt.date
df = df[(df['facility_name'] == 'STREET CHURROS') & (df['score'] < 95)]
df = df[['activity_date', 'pe_description']]
df