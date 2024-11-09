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