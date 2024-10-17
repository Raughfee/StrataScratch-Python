# Import your libraries
import pandas as pd

# Start writing code
df = car_launches.copy()
df1 = df[df['year'] == 2020].groupby('company_name')['product_name'].count().reset_index()
df2 = df[df['year'] == 2019].groupby('company_name')['product_name'].count().reset_index()
df = pd.merge(df1,df2, how = 'left', on = 'company_name')
df['net_new_products'] = df['product_name_x'] - df['product_name_y']
df = df[['company_name', 'net_new_products']]
df