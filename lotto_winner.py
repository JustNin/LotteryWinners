import pandas as pd

# Load CSV from same folder
df = pd.read_csv('Numbers_2002.csv')

# Take last 100 draws (most recent first)
df_last_100 = df.head(100)

# Show it
print(df_last_100)
print(df_last_100['Winning Numbers'].value_counts())
