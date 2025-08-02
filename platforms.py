import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
df = pd.read_csv('spotify-2023.csv', encoding='latin1')

# Clean and convert streams column
df['streams'] = df['streams'].astype(str).str.replace(',', '')
df['streams'] = pd.to_numeric(df['streams'], errors='coerce')

# Drop rows with invalid streams
df = df.dropna(subset=['streams'])
df['streams'] = df['streams'].astype(int)


platform_cols = [
    'in_spotify_playlists', 'in_spotify_charts',
    'in_apple_playlists', 'in_apple_charts',
    'in_deezer_playlists', 'in_deezer_charts',
    'in_shazam_charts'
]

# Convert platform columns to numeric, coercing errors to NaN then filling NaNs with 0
for col in platform_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

presence_summary = df[platform_cols].sum().sort_values(ascending=False)
print("Number of songs present on each platform/playlist/chart:")
print(presence_summary)


# Create a new column counting how many platforms each song appears on
df_presence = df[platform_cols].gt(0).astype(int)
df['platform_presence_count'] = df_presence.sum(axis=1)
print(df[['track_name', 'platform_presence_count', 'streams']].head())


# Analyze average streams by platform presence count
avg_streams_by_presence = df.groupby('platform_presence_count')['streams'].mean()
print(avg_streams_by_presence)

# plot it
avg_streams_by_presence.plot(kind='bar', figsize=(10,6), color='dodgerblue')
plt.title('Average Streams by Number of Platforms Present On')
plt.xlabel('Number of Platforms Present On')
plt.ylabel('Average Streams')
plt.xticks(rotation=0)
plt.show()

median_streams = df.groupby('platform_presence_count')['streams'].median()

median_streams.plot(kind='bar', figsize=(10,6), color='orange')
plt.title('Median Streams by Number of Platforms Present On')
plt.xlabel('Number of Platforms Present On')
plt.ylabel('Median Streams')
plt.show()

# Scatter plot with some jitter on x-axis


plt.figure(figsize=(10,6))
plt.scatter(df['platform_presence_count'] + np.random.normal(0, 0.1, size=len(df)), df['streams'], alpha=0.3)
plt.title('Streams vs. Number of Platforms Present On')
plt.xlabel('Number of Platforms Present On')
plt.ylabel('Streams')
plt.yscale('log')  # Log scale because streams vary hugely
plt.show()