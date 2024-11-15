# Convert the relevant parts of your notebook into a Python script
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr
import gdown
import os

def download_dataset():
    if not os.path.exists('song_dataset.csv'):
        file_id = "1MKqJmWQ1PxKHDkpIdbQEeTz_ohpjOsYPyVp6esEZsq4"
        url = f"https://drive.google.com/uc?id={file_id}"
        # Download as Excel first
        gdown.download(url, 'temp_dataset.xlsx', quiet=False)
        # Convert Excel to CSV
        temp_df = pd.read_excel('temp_dataset.xlsx')
        temp_df.to_csv('song_dataset.csv', index=False)
        # Remove temporary Excel file
        os.remove('temp_dataset.xlsx')

# Download dataset
download_dataset()

# Load the data
df = pd.read_csv('song_dataset.csv')

# Create user-song matrix
interaction_matrix = df.pivot_table(
    index='user',
    columns='song',
    values='play_count',
    fill_value=0
)

def search_songs(query):
    if not query or len(query) < 2:
        return gr.update(choices=[])
    try:
        matches = song_choices[
            song_choices['display'].str.lower().str.contains(query.lower(), regex=False)
        ]['display'].tolist()
        return gr.update(choices=matches[:10])
    except Exception as e:
        print(f"Search error: {e}")
        return gr.update(choices=[])

def add_to_selection(new_song, current_selections):
    if not current_selections:
        current_selections = []
    
    if new_song and new_song not in current_selections and len(current_selections) < 5:
        current_selections.append(new_song)
    
    return gr.update(choices=current_selections, value=current_selections)

def make_recommendations(selected_songs, n_recommendations=5):
    if not selected_songs:
        return "Please select at least one song to get recommendations."
        
    temp_user_profile = pd.Series(0, index=interaction_matrix.columns)
    for song in selected_songs:
        song_id = song_choices[song_choices['display'] == song]['song'].iloc[0]
        temp_user_profile[song_id] = 1
    
    user_sim = cosine_similarity([temp_user_profile], interaction_matrix)[0]
    
    unheard_songs = list(set(interaction_matrix.columns) - 
                        set([song_choices[song_choices['display'] == song]['song'].iloc[0] 
                             for song in selected_songs]))
    
    pred_ratings = []
    for song in unheard_songs:
        pred = np.sum(user_sim * interaction_matrix[song]) / np.sum(np.abs(user_sim))
        pred_ratings.append((song, pred))
    
    ratings = np.array([r[1] for r in pred_ratings])
    if len(ratings) > 0:
        min_rating, max_rating = ratings.min(), ratings.max()
        if max_rating > min_rating:
            normalized_ratings = 1 + 4 * (ratings - min_rating) / (max_rating - min_rating)
        else:
            normalized_ratings = [3.0] * len(ratings)
    else:
        return "No recommendations found for the selected songs."
    
    recommendations = list(zip([r[0] for r in pred_ratings], normalized_ratings))
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:n_recommendations]
    
    output = ""
    for song_id, rating in recommendations:
        song_details = df[df['song'] == song_id].iloc[0]
        output += f"Title: {song_details['title']}\n"
        output += f"Artist: {song_details['artist_name']}\n"
        output += f"Year: {song_details['year']}\n"
        output += f"Rating: {rating:.2f}/5.00\n"
        output += "-" * 50 + "\n"
    
    return output

# Create song choices for dropdown
song_choices = df[['song', 'title', 'artist_name']].drop_duplicates()
song_choices['display'] = song_choices['title'] + " - " + song_choices['artist_name']
song_list = song_choices['display'].tolist()

# Create Gradio interface
with gr.Blocks(title="Wanna Be Spotify") as iface:
    gr.Markdown("# 🎵 Wanna Be Spotify")
    gr.Markdown("Search and select up to 5 songs you've enjoyed to get personalized recommendations!")
    
    with gr.Row():
        search_box = gr.Textbox(
            label="Search for songs",
            placeholder="Type song or artist name...",
            show_label=True
        )
    
    with gr.Row():
        search_results = gr.Radio(
            choices=[],
            label="Search Results",
            interactive=True,
            show_label=True
        )
    
    with gr.Row():
        selected_songs = gr.Dropdown(
            choices=[],
            label="Selected Songs",
            interactive=True,
            multiselect=True,
            max_choices=5,
            show_label=True
        )
    
    with gr.Row():
        recommendations = gr.Textbox(
            label="Recommendations",
            interactive=False,
            lines=10,
            show_label=True
        )
    
    submit_btn = gr.Button("Get Recommendations")

    search_box.change(
        fn=search_songs,
        inputs=[search_box],
        outputs=[search_results]
    )
    
    search_results.change(
        fn=add_to_selection,
        inputs=[search_results, selected_songs],
        outputs=[selected_songs]
    )
    
    submit_btn.click(
        fn=make_recommendations,
        inputs=[selected_songs],
        outputs=[recommendations]
    )

# Launch the interface
iface.launch()