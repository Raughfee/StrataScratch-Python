# Import your libraries
import pandas as pd

# Start writing code
df = fb_friend_requests.copy()
df['date'] = pd.to_datetime(df['date']).dt.date
df1 = df[df['action'] == 'sent']
df2 = df[df['action'] == 'accepted']
df3 = pd.merge(df1, df2, how = 'left', left_on = ['user_id_sender', 'user_id_receiver'],
right_on = ['user_id_sender', 'user_id_receiver'])
df3 = df3.groupby('date_x')['action_x','action_y'].count().reset_index()
df3['percentages'] = df3['action_y']/ df3['action_x']
df3 = df3.rename(columns = {'date_x': 'date'})
df3 = df3[['date', 'percentages']]