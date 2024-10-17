import pandas as pd

# Assuming df is your DataFrame containing the 'sf_events' data
df = sf_events
# Convert 'date' to datetime if it's not already
df['date'] = pd.to_datetime(df['date'])

# Define the condition for December retention users
dec_ret_users = df[df['date'].dt.to_period('M') == '2020-12']['user_id'].drop_duplicates()

# Define the DataFrame for December retention
dec_ret = df[(df['date'].dt.to_period('M') > '2020-12') & df['user_id'].isin(dec_ret_users)]
dec_ret = dec_ret[['account_id', 'user_id']].drop_duplicates()

# Define the condition for January retention users
jan_ret_users = df[df['date'].dt.to_period('M') == '2021-01']['user_id'].drop_duplicates()

# Define the DataFrame for January retention
jan_ret = df[(df['date'].dt.to_period('M') > '2021-01') & df['user_id'].isin(jan_ret_users)]
jan_ret = jan_ret[['account_id', 'user_id']].drop_duplicates()

# Perform a left join on 'account_id'
retention_df = dec_ret.merge(jan_ret, on='account_id', how='left', suffixes=('_dec', '_jan'))

# Calculate retention rates
retention_df = retention_df.groupby('account_id').agg(
    dec_count=('user_id_dec', 'count'),
    jan_count=('user_id_jan', 'count')
)

retention_df['retention'] = retention_df['jan_count'] / retention_df['dec_count']

# Reset index to make 'account_id' a column again if needed
retention_df.reset_index(inplace=True)

# Display the result
df1 = retention_df[['account_id', 'retention']]
df1
