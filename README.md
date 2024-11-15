# 🎸 Song Recommendation Engine ✨

A data-driven music recommendation system that analyzes listening patterns and suggests new songs to users. Using collaborative filtering and machine learning techniques, this system provides personalized music recommendations based on user preferences.

## 🎯 Live Demos
- **Hugging Face Space**: [Not Spotify But Close](https://huggingface.co/spaces/GouthamVarma/not-spotify-but-close)
- **GitHub Repository**: [Song Recommendation Engine](https://github.com/GouthamVarmaI/Song-Recommendation-Engine)

## Project Overview

This project consists of three main phases:
1. ✅ **Exploratory Data Analysis (EDA)**
   - Analysis of user listening patterns
   - Song popularity distribution
   - Artist and genre insights
   
2. ✅ **Recommendation Engine Development**
   - Collaborative filtering implementation
   - Similarity matrix computation
   - Rating prediction system
   
3. ✅ **Web Platform Deployment**
   - Gradio interface development
   - Hugging Face Spaces deployment
   - Real-time recommendations

## Deployments

### 1. Hugging Face Space (Web Demo)
- Interactive web interface for quick song recommendations
- No installation required
- Real-time song search and recommendations
- User-friendly interface
- Try it out: [Not Spotify But Close](https://huggingface.co/spaces/GouthamVarma/not-spotify-but-close)

### 2. GitHub Repository (Full Project)
- Complete source code and development notebooks
- Dataset and analysis tools
- Documentation and setup instructions
- Perfect for developers and data scientists

## Project Structure
```
Song-Recommendation-Engine/       # Main GitHub repository
├── data/                         # Dataset directory
│   └── song_dataset.csv          # Main dataset with user-song interactions
├── notebooks/                    # Jupyter notebooks
│   └── engine.ipynb              # Analysis and model development notebook
├── huggingface-demo/             # Hugging Face Space deployment
│   ├── app.py                    # Gradio web interface implementation
│   ├── requirements.txt          # Space dependencies
│   └── README.md                 # Space documentation
└── README.md                     # Main repository documentation
```

## Setup Instructions

### Quick Start (Web Demo)
1. Visit [Not Spotify But Close](https://huggingface.co/spaces/GouthamVarma/not-spotify-but-close)
2. Search for songs you like using the search bar
3. Select up to 5 songs from your search results
4. Click "Get Recommendations" to receive personalized suggestions

### Local Development Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/GouthamVarmaI/Song-Recommendation-Engine.git
   cd Song-Recommendation-Engine
   ```

2. Create and activate a virtual environment:
   ```bash
   # Using conda
   conda create -n song-rec python=3.9
   conda activate song-rec

   # OR using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

5. Open `notebooks/engine.ipynb` to explore the development process

### Running the Web Interface Locally
1. Navigate to the huggingface-demo directory:
   ```bash
   cd huggingface-demo
   ```

2. Install additional requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Gradio app:
   ```bash
   python app.py
   ```

## Tech Stack
- **Python**: Primary programming language
- **Data Processing**:
  - Pandas & NumPy for data manipulation
  - Scikit-learn for similarity calculations
- **Web Interface**:
  - Gradio for interactive UI
  - Hugging Face Spaces for deployment
- **Development**:
  - Jupyter Notebooks for analysis
  - Git for version control

## Features
- 🔍 Fast song search functionality
- 🎯 Personalized recommendations based on user selections
- 📊 Detailed song information including artist and year
- 🚀 Real-time recommendation generation
- 📱 Responsive web interface

## Dataset
The project uses a comprehensive dataset containing:
- User listening histories
- Song metadata (title, artist, year)
- Play count information
- Over 100,000 user-song interactions

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Dataset sourced from [Last.fm](http://www.last.fm/)
- Inspired by modern music recommendation systems
- Built with open-source tools and libraries