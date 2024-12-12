# Music Recommendation System

A music recommendation system built using matrix factorization and deployed on Hugging Face Spaces.

## Overview
This application provides music recommendations based on user-selected songs. It uses truncated SVD for matrix factorization to generate recommendations.

## How to Use
1. Select up to 5 songs you like from the dropdown menu
2. Click "Get Recommendations" to see similar songs
3. Each recommendation comes with a confidence score

## Technical Details
- Built using Python, Gradio, and scikit-learn
- Uses TruncatedSVD for matrix factorization
- Deployed on Hugging Face Spaces