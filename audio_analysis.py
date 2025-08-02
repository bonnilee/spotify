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

# Summary Statistics of Audio Features
audio_features = [
    'danceability_%', 'energy_%', 'valence_%', 'acousticness_%',
    'instrumentalness_%', 'liveness_%', 'speechiness_%', 'bpm'
]

print(df[audio_features].describe())

# Visualize Distributions of Audio Features
plt.figure(figsize=(12, 8))
df[audio_features].hist(bins=20, layout=(3, 3))
plt.tight_layout()
plt.show()

# Correlation Between Audio Features and Streams
corr = df[audio_features + ['streams']].corr()
print(corr['streams'].sort_values(ascending=False))


# Visualize the correlation matrix as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
plt.title("Correlation between Audio Features and Streams")
plt.show()
