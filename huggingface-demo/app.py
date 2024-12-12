import gradio as gr
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
import time
from model import MatrixFactorization

# Load the preprocessed data
df = pd.read_csv('data.csv')

# Initialize and train the model
mf_recommender = MatrixFactorization(n_factors=100)
mf_recommender.fit(df)

# Create and launch the Gradio interface
demo = create_gradio_interface(mf_recommender)
demo.launch()