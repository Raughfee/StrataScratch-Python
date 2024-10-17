# Import your libraries
import pandas as pd
from math import ceil

# Start writing code
df = fraud_score.copy()
df['count'] = df.groupby('state')['state'].transform('count')
df['rank'] = df.groupby('state')['fraud_score'].rank(method = 'first', ascending = False)
df = df.sort_values(by = ['state', 'fraud_score'], ascending = (True, False))
df = df[df['rank'] <=  (df['count']* 1/20).apply(ceil)] 
df = df[['policy_num', 'state', 'claim_cost', 'fraud_score']]
df