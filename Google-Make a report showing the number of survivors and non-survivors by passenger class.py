# Import your libraries
import pandas as pd

# Start writing code
df = titanic.copy()
df['first_class'] = df['pclass'].apply(lambda x: 1 if x == 1 else 0)
df['second_class'] = df['pclass'].apply(lambda x: 1 if x == 2 else 0)
df['third_class'] = df['pclass'].apply(lambda x: 1 if x == 3 else 0)
df = df[['survived', 'first_class', 'second_class', 'third_class']]
df = df.groupby('survived').agg({'first_class':'sum', 'second_class':'sum',
    'third_class': 'sum'
}).reset_index()
df