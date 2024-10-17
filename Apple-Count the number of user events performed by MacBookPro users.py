# Import your libraries
import pandas as pd

# Start writing code
df = playbook_events.copy()
df = df[df['device'] == 'macbook pro']
df = df.groupby('event_name')['user_id'].count().reset_index(name = 'event_count').sort_values(by= 'event_count', ascending = False)
df