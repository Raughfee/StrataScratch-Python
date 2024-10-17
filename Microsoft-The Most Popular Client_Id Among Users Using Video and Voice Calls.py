# Import your libraries
import pandas as pd

# Start writing code
df = fact_events.copy()
df = df.groupby('user_id').apply(
    lambda x: (x['event_type'].isin(['video call received', 'video call sent', 'voice call received', 'voice call sent']).mean())
).reset_index(name='avg_event')
df = df[df['avg_event'] >= 0.5]['user_id']

fact_events = fact_events[fact_events['user_id'].isin(df)]
client_event_count = fact_events.groupby('client_id')['client_id'].count().reset_index(name='event_count')
client_event_count['rank'] = client_event_count['event_count'].rank(method='dense', ascending=False)

client_event_count = client_event_count[client_event_count['rank'] == 1][['client_id']]