import streamlit as st
import pandas as pd
import requests
import pickle

# Load the processed data and similarity matrix
with open('movie_data.pkl', 'rb') as file:
    movies, cosine_sim = pickle.load(file)

# Function to get movie recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Get top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Fetch movie poster from TMDB API
def fetch_poster(movie_id):
    api_key = '7b995d3c6fd91a2284b4ad8cb390c7b8'  
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500{poster_path}"
    return full_path

# Streamlit UI
st.set_page_config(page_title="🎬 Movie Recommendation System", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Center the title */
        .title {
            text-align: center;
            font-size: 50px;  
            font-weight: 800;
            margin-bottom: 10px;
        }

        /* Subtitle styling */
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #666;
            margin-bottom: 40px;
        }

        /* Movie card */
        .movie-card {
            text-align: center;
            padding: 15px;
            border-radius: 16px;
            background: white;
            box-shadow: 0px 6px 16px rgba(0,0,0,0.12);
            transition: transform 0.2s ease-in-out;
            margin-bottom: 30px;   /* Added spacing between rows */
        }

        /* Hover effect */
        .movie-card:hover {
            transform: translateY(-8px);
            box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
        }

        /* Poster image */
        .movie-poster {
            width: 160px;
            height: 240px;
            border-radius: 12px;
            object-fit: cover;
            margin-bottom: 12px;
        }

        /* Movie title */
        .movie-title {
            font-size: 15px;
            font-weight: 600;
            color: #222;
            line-height: 1.2;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="title">🍿 Movie Recommendation System</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Select a movie you like and discover 10 similar ones!</p>', unsafe_allow_html=True)

# Select movie
selected_movie = st.selectbox("🎬 Choose a movie:", movies['title'].values)

# Button
if st.button('✨ Get Recommendations'):
    recommendations = get_recommendations(selected_movie)
    st.markdown("🎯 Top 10 Recommendations")
    st.markdown("---")

    # Display in 2x5 grid
    for i in range(0, 10, 5):
        cols = st.columns(5, gap="large")
        for col, j in zip(cols, range(i, i+5)):
            if j < len(recommendations):
                movie_title = recommendations.iloc[j]['title']
                movie_id = recommendations.iloc[j]['movie_id']
                poster_url = fetch_poster(movie_id)

                with col:
                    st.markdown(
                        f"""
                        <div class="movie-card">
                            <img class="movie-poster" src="{poster_url}">
                            <p class="movie-title">{movie_title}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

        # Vertical spacing between rows
        st.markdown("<br>", unsafe_allow_html=True)
