# Import your libraries
import pandas as pd

# Start writing code
df = cookbook_titles.copy()
df['left_page'] = (df['page_number'].rank(method = 'min', ascending = True) -1)*2
df['right_page'] = (df['page_number'].rank(method = 'min', ascending = True) -1)*2 +1
df1 = pd.merge(df, cookbook_titles, how = 'left', left_on = 'left_page', right_on = 'page_number')
df1 = pd.merge(df1, cookbook_titles, how  = 'left', left_on = 'right_page', right_on = 'page_number')
df1 = df1[['left_page', 'title_y', 'title']]
df1 = df1.rename(columns = {'title_y': 'left_title', 'title': 'right_title'})
df1