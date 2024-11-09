# Music Listening Analysis

This project analyzes user listening patterns using a comprehensive dataset of song plays. The dataset encompasses information about users, songs, artists, and play counts, providing a rich foundation for exploration.

## Project Overview
The analysis undertaken in this project encompasses a range of aspects, including:
- Identification of top songs and artists based on play count
- Examination of user listening patterns to understand their preferences
- Analysis of the temporal distribution of songs to identify trends over time
- Assessment of data quality to ensure the integrity of the findings

## Setting Up the Project
To replicate this analysis, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.

**Dataset Location**
Please ensure the `song_dataset.csv` file is placed in the `data` folder within the project directory.

**Project Structure**
- `data/`: This folder contains the dataset used for analysis. Note that the dataset is not tracked in the Git repository.
- `notebooks/`: This folder houses Jupyter notebooks that contain the analysis and visualizations.
- `requirements.txt`: This file lists the project dependencies required for the analysis.

## Key Insights
The analysis has yielded several interesting findings, including:
- The majority of users tend to listen to a relatively small number of unique songs.
- A strong recency bias is evident in the dataset, with a significant proportion of plays occurring between 2000 and 2010.
- Approximately 18.8% of songs in the dataset have missing year data.
- Kings of Leon emerge as the most played artist in the dataset.
