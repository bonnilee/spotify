import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('spotify-2023.csv', encoding='latin1')

# Clean and convert streams column
df['streams'] = df['streams'].astype(str).str.replace(',', '')
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# Drop rows with invalid streams
df = df.dropna(subset=['streams'])
df['streams'] = df['streams'].astype(int)

# Now you can safely group and plot
artist_counts = df['artist(s)_name'].value_counts().head(10)
print("Top 10 Artists by Number of Songs:")
print(artist_counts)

artist_streams = df.groupby('artist(s)_name')['streams'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Artists by Total Streams:")
print(artist_streams)

artist_streams.plot(kind='barh', figsize=(10,6), color='skyblue')
plt.title("Top 10 Artists by Total Streams")
plt.xlabel("Total Streams")
plt.ylabel("Artist")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()


