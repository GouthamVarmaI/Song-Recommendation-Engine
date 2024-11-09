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
   cd Song-Recommendation-Engine
   ```

2. Create and activate virtual environment:
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # Windows
   venv\Scripts\activate
   # Unix/MacOS
   source venv/bin/activate

   # Verify activation (optional)
   # Should show virtual environment python path
   which python  # Unix/MacOS
   where python  # Windows
   ```

3. Install requirements:
   ```bash
   # Upgrade pip first (recommended)
   python -m pip install --upgrade pip

   # Install requirements
   pip install -r requirements.txt

   # Note: If you encounter conflicts, try:
   pip install typing-extensions==4.5.0
   pip install -r requirements.txt --no-deps
   pip install scikit-learn numpy pandas matplotlib seaborn plotly
   ```

4. Install Jupyter (if not already installed):
   ```bash
   pip install jupyter
   ```

5. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/engine.ipynb
   ```

### Troubleshooting
- If you encounter dependency conflicts:
  - Make sure you're using a fresh virtual environment
  - Try installing packages one by one
  - Check if your Python version is 3.8 or higher
  - If using Anaconda, consider creating a new conda environment instead

### Note on Dependencies
The project requires specific versions of some packages to avoid conflicts:
- typing-extensions==4.5.0 (required for tensorflow compatibility)
- gradio==3.35.0
- Other packages (numpy, pandas, etc.) can use latest versions

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