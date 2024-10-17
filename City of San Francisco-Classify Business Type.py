# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations.copy()
df['restaurant'] = df['business_name'].str.contains('restaurant', case = False, regex = True)
df['cafe'] = df['business_name'].str.contains('cafe|café|coffee', case=False, regex=True)
df['school'] = df['business_name'].str.contains('school', case=False, regex=True)
df['other'] = ~(df['restaurant'] | df['cafe'] | df['school'])
def determine_business_type(row):
    if row['restaurant']:
        return 'restaurant'
    elif row['cafe']:
        return 'cafe'
    elif row['school']:
        return 'school'
    else:
        return 'other'

# Apply the function to each row to create the 'business_type' column
df['business_type'] = df.apply(determine_business_type, axis=1)
df = df[['business_name', 'business_type']].drop_duplicates()
df