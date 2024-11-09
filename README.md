# Song Recommendation Engine

A data-driven music recommendation system that analyzes listening patterns and suggests new songs to users.

## Project Overview

This project consists of three main phases:
1. ✅ Exploratory Data Analysis (EDA)
2. 🚧 Recommendation Engine Development
3. 🔜 Web Platform Deployment

## Current Progress

### Completed: Data Analysis
- Analyzed user listening patterns and preferences
- Identified top songs and artists
- Examined song count distribution across users
- Discovered temporal trends in music releases
- Generated visualizations for key insights

### Key Findings
- Most users listen to a concentrated set of songs
- Strong temporal patterns in listening behavior
- Identified popular artists and their impact
- Analyzed user engagement patterns
- Discovered interesting correlations between release years and popularity

## Project Structure
- `data/` 
  - `song_dataset.csv` - Main dataset containing user listening history
- `notebooks/`
  - `engine.ipynb` - Contains the data analysis and visualizations
- `requirements.txt` - Project dependencies

## Dataset Description
The dataset contains:
- User IDs for each listener
- Song IDs and titles
- Listen counts per user-song pair
- Album information
- Artist details
- Release years

## Getting Started
1. Clone this repository
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Open `notebooks/engine.ipynb` to view the analysis

## Next Steps
1. Develop recommendation algorithm
   - Implement user-based collaborative filtering
   - Consider content-based approaches
   - Evaluate different recommendation strategies

2. Create web platform
   - Build user interface with dropdown menus
   - Implement recommendation API
   - Deploy platform for public access

## Tech Stack
- Python
- Pandas & NumPy for data analysis
- Matplotlib & Seaborn for visualizations
- Jupyter Notebooks for development

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
