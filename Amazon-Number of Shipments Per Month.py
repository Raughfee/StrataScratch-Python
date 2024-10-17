# Import your libraries
import pandas as pd

# Start writing code
df = amazon_shipment.copy()
df['shipment_date'] = pd.to_datetime(df['shipment_date']).dt.strftime('%Y-%m')
df = df.groupby('shipment_date')['shipment_id'].count().reset_index(name = 'count' )
df