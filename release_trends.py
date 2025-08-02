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


# Analyze number of songs released by year
release_year_counts = df['released_year'].value_counts().sort_index()

print("Songs released per year:")
print(release_year_counts)

# Plot it
release_year_counts.plot(kind='bar', figsize=(10,5), color='mediumseagreen')
plt.title('Number of Songs Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Songs')
plt.show()

# Analyze number of songs released by month (across all years)
release_month_counts = df['released_month'].value_counts().sort_index()

print("Songs released per month:")
print(release_month_counts)

# Plot it
release_month_counts.plot(kind='bar', figsize=(10,5), color='coral')
plt.title('Number of Songs Released per Month (All Years Combined)')
plt.xlabel('Month')
plt.ylabel('Number of Songs')
plt.show()


#Combine year and month to see trends over time
df['release_date'] = pd.to_datetime({
    'year': df['released_year'],
    'month': df['released_month'],
    'day': df['released_day']
})




# plot it
monthly_releases = df.groupby(pd.Grouper(key='release_date', freq='ME')).size()
monthly_releases.plot(figsize=(12,6), color='purple')
plt.title('Number of Songs Released per Month Over Time')
plt.xlabel('Release Date')
plt.ylabel('Number of Songs')
plt.show()
