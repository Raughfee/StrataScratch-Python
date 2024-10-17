# Import your libraries
import pandas as pd
import numpy as np

df = premium_accounts_by_day.copy()

df['entry_date_7'] = df['entry_date'] + pd.DateOffset(7)
df = pd.merge(df, df, how = 'left', left_on = ['account_id', 'entry_date_7'], right_on = ['account_id', 'entry_date'])
df= df[df['final_price_x'] > 0]
df['final_price_y']= df['final_price_y'].replace({0: np.nan})
df= df.groupby('entry_date_x').count()[['final_price_x', 'final_price_y']].reset_index().head(7)