import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
import time

class MatrixFactorization:
    def __init__(self, n_factors=100):
        self.n_factors = n_factors
        self.model = TruncatedSVD(n_components=n_factors, random_state=42)
        self.user_title_matrix = None
        self.titles_df = None
        
    def fit(self, df):
        print("Training model...")
        start_time = time.time()
        
        self.user_title_matrix = pd.pivot_table(
            df,
            values='play_count',
            index='user',
            columns='title',
            fill_value=0
        )
        
        self.titles_df = df.groupby('title').agg({
            'artist_name': 'first',
            'year': 'first',
            'play_count': 'sum',
            'release': 'first'
        })
        
        self.user_vectors = self.model.fit_transform(self.user_title_matrix)
        self.item_vectors = self.model.components_
        
        train_time = time.time() - start_time
        print(f"Training completed in {train_time:.2f} seconds")
        print(f"Matrix shape: {self.user_title_matrix.shape}")
        print(f"Explained variance ratio: {self.model.explained_variance_ratio_.sum():.4f}")

    def get_recommendations_from_titles(self, selected_display_titles, n_recommendations=5):
        try:
            actual_titles = [display.split(" • by ")[0] for display in selected_display_titles]
            
            title_to_idx = {title: idx for idx, title in enumerate(self.user_title_matrix.columns)}
            selected_indices = [title_to_idx[title] for title in actual_titles]
            
            user_vector = np.zeros((1, self.n_factors))
            for idx in selected_indices:
                user_vector += self.item_vectors[:, idx].reshape(1, -1)
            user_vector = user_vector / len(selected_indices)
            
            predicted_ratings = np.dot(user_vector, self.item_vectors)
            predicted_ratings = predicted_ratings.flatten()
            
            titles = self.user_title_matrix.columns
            title_scores = [(title, score) for title, score in zip(titles, predicted_ratings)
                          if title not in actual_titles]
            
            recommendations = sorted(title_scores, key=lambda x: x[1], reverse=True)[:n_recommendations]
            
            scores = np.array([score for _, score in recommendations])
            confidence_scores = ((scores - scores.min()) / (scores.max() - scores.min()) * 80 + 20)
            
            results = []
            for (title, _), conf in zip(recommendations, confidence_scores):
                row = self.titles_df.loc[title]
                results.append([title, row['artist_name'], int(row['year']) if pd.notna(row['year']) else None, f"{conf:.2f}%"])
            
            return results
        except Exception as e:
            print(f"Error in recommendations: {str(e)}")
            return []

def create_gradio_interface(mf_model):
    def get_recommendations(selected_titles):
        if not selected_titles:
            return []
        return mf_model.get_recommendations_from_titles(selected_titles)

    title_choices = []
    for title, row in mf_model.titles_df.iterrows():
        display_text = f"{title} • by {row['artist_name']}"
        
        extra_info = []
        if pd.notna(row['release']):
            extra_info.append(row['release'])
        if pd.notna(row['year']):
            extra_info.append(str(int(row['year'])))
        
        if extra_info:
            display_text += f" [{', '.join(extra_info)}]"
            
        title_choices.append(display_text)

    with gr.Blocks() as demo:
        gr.Markdown("""# Music Recommendation System""")
        
        input_songs = gr.Dropdown(
            choices=sorted(title_choices),
            label="Select songs you've listened to",
            multiselect=True,
            max_choices=5
        )
        
        recommend_btn = gr.Button("Get Recommendations")
        output_table = gr.DataFrame(
            headers=["Song", "Artist", "Year", "Confidence"],
            label="Recommended Songs"
        )
        
        recommend_btn.click(fn=get_recommendations, inputs=input_songs, outputs=output_table)
    
    return demo