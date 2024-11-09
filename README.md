# Song Recommendation Engine

A data-driven music recommendation system that analyzes listening patterns and suggests new songs to users.

## Project Overview

This project consists of three main phases:
1. ✅ Exploratory Data Analysis (EDA)
2. ✅ Recommendation Engine Development
3. ✅ Web Platform Deployment

## Current Progress

### Completed: Data Analysis & Engine Development
- Analyzed user listening patterns and preferences
- Identified and handled missing data
- Implemented collaborative filtering recommendation system
- Deployed interactive web interface using Gradio
- Normalized ratings and improved recommendation quality

### Key Features
- User-based song recommendations
- Interactive song selection interface
- Rating predictions on a 1-5 scale
- Artist and year information included
- Fast and efficient recommendation generation

## Project Structure
- `data/` 
  - `song_dataset.csv` - Main dataset containing user listening history
- `notebooks/`
  - `engine.ipynb` - Contains the data analysis and recommendation engine
- `requirements.txt` - Project dependencies

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Song-Recommendation-Engine.git
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Unix/MacOS
   source venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/engine.ipynb
   ```

## Using the Recommendation Engine
1. Open the notebook and run all cells
2. The Gradio interface will launch
3. Select songs you like from the dropdown menu
4. Get personalized recommendations based on your selections

## Tech Stack
- Python
- Pandas & NumPy for data processing
- Scikit-learn for similarity calculations
- Gradio for web interface
- Jupyter Notebooks for development

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.