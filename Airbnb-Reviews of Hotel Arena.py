# Import your libraries
import pandas as pd

# Start writing code
df = hotel_reviews.copy()
df = df[df['hotel_name'] == 'Hotel Arena']
df  = df.groupby(['hotel_name','reviewer_score'])['positive_review'].count().reset_index(name = 'n_reviews' )
df