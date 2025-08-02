readme_content = """
# Most Streamed Spotify Songs 2023 Analysis

## Project Overview
This project analyzes the "Most Streamed Spotify Songs 2023" dataset to explore various aspects of popular songs on Spotify and other platforms. The dataset includes detailed song attributes, streaming counts, release information, and platform presence.

## Setup
- Python 3.12 with `pipenv` virtual environment
- Key libraries: `pandas`, `matplotlib`, `seaborn`
- Dataset CSV file: `spotify-2023.csv`

## Data Loading and Cleaning
- Loaded CSV with encoding `latin1` to handle special characters.
- Cleaned the `streams` column by removing commas and converting it to integers.
- Handled any invalid stream values by coercing errors and dropping problematic rows.

## Analysis Steps

### 1. Top Artists by Streams and Song Counts
- Aggregated total streams by artist.
- Identified top artists by number of songs and total streams.
- Visualized the top 10 artists by total streams using a horizontal bar chart.
- The top ten artists were - The Weekend, Taylor Swift, Ed Sheeran, Harry Styles,
  Bad Bunny, Olivia Rodrigo, Eminem, Bruno Mars, Artic Monkeys, and Imagine Dragons.

### 2. Audio Feature Analysis
- Analyzed audio features such as danceability, energy, valence, acousticness, instrumentalness, liveness, speechiness, and bpm.
- Summarized these features with descriptive statistics.
- Visualized distributions using histograms.
- Explored correlations between audio features and streams, visualized with a     heatmap.
- Most songs have moderate to high danceability (mean ~67%).

- Energy values are generally mid-to-high (~64%), showing the songs tend to be fairly energetic.

- Valence (happiness) is about 51% on average, so songs are about neutral in mood.

- BPM varies widely from slow (~65 bpm) to very fast (~206 bpm), with a median near 121 bpm — typical for many popular songs.

### 3. Release Trends
- Explored song release distribution by year and month.
- Created a proper `release_date` column by combining year, month, and day.
- Visualized monthly song release trends over time.
- Songs Released per Year:

- The dataset includes songs released as far back as 1930 and up to 2023.

 Most songs in the dataset are recent — a big jump starting around 2019, especially 2021 (119 songs), 2022 (402 songs), and 2023 (175 songs).

 This shows the dataset heavily features current hits, but also includes some older classics still popular or re-streamed.

- Songs Released per Month (Across All Years):

January and May see the highest number of song releases (~130 each).

The lowest counts are in August (46 songs) and September (56 songs).

This might reflect industry trends or release strategies (e.g., more releases at year-start or before summer).

### 4. Platform Presence Analysis
- Analyzed how many songs appear on various platforms and charts (Spotify, Apple Music, Deezer, Shazam).
- Cleaned platform presence columns by converting to numeric.
- Summarized and visualized counts and percentages of songs present on each platform/chart.

### 5. Comparing Platform Presence and Streams
- Created a new feature counting how many platforms each song is present on.
- Analyzed average and median streams by the number of platforms present.
- Visualized relationships with bar charts and scatter plots (log scale for streams).
- More platform presence generally means more streams. Songs on 5 or 6 platforms average over 600 million streams — much higher than songs present on just 1 or 2 platforms.

But presence on all 7 platforms doesn't guarantee the absolute highest streams. Interestingly, songs on exactly 7 platforms have slightly lower average streams than those on 5 or 6 platforms. This could be due to outliers or specific artist/genre differences.

There is a big jump in streams moving from 1-4 platforms to 5-6 platforms, suggesting strong benefits in reaching more platforms.

Presence is an important but not the only factor influencing streams, as other things like artist popularity, playlist type, and promotion matter.

## How to Run
1. Activate your virtual environment with `pipenv shell`.
2. Run your script (e.g., `python main.py`).
3. Follow the outputs and visualizations generated for insights.

## Next Steps (Suggestions)
- Explore clustering songs by audio features to identify distinct “vibe” groups.
- Compare streaming success based on release timing or playlists.
- Dive deeper into how specific audio features influence popularity.

---
"""

with open("/mnt/data/README.md", "w") as f:
    f.write(readme_content)
