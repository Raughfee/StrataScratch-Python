# Import your libraries
import pandas as pd

# Start writing code
df = winemag_p1.copy()
df = df[df['description'].str.contains(r'\b(plum|rose|hazelnut|cherry)\b', case = False, 
     regex = True)][['winery']].drop_duplicates().sort_values( by = 'winery', ascending = True)