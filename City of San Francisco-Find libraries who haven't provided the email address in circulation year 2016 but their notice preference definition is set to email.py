# Import your libraries
import pandas as pd

# Start writing code
df = library_usage.copy()
df = df[(df['provided_email_address'] == False) &(df['notice_preference_definition'] == 'email') & (df['circulation_active_year'] == 2016)][['home_library_code']].drop_duplicates()
df