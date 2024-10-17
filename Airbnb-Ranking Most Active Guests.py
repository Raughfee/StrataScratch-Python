# Import your libraries
import pandas as pd

# Start writing code
df = airbnb_contacts.copy()
df = df.groupby('id_guest')['n_messages'].sum().reset_index().sort_values(by = ['n_messages'], ascending = False)
df['ranking'] = df['n_messages'].rank(method = 'dense', ascending = False)
df