# Movie Recommendation System
This project is a Movie Recommendation System built with Streamlit and powered by a machine learning model. It recommends movies similar to a selected title using cosine similarity and displays their posters fetched from the TMDB API.

# Overview

- The Movie Recommendation System helps users discover movies similar to their favorites.
- Select a movie from the dropdown list
- Get Top 10 recommended movies based on similarity
- View movie posters (via TMDB API) alongside recommendations
- Built with Streamlit for an interactive and user-friendly interface

# Cosine Similarity

Cosine similarity is used to measure how alike two movies are:
- Each movie is represented as a vector of features
- The similarity score is the cosine of the angle between these vectors
- Higher scores mean the movies are more similar
- The model recommends the Top 10 most similar movies

# Dataset

The dataset used contains metadata of movies (titles, IDs, etc.).
Files provided:

- movies.csv -→ Contains details of movies
- credits.csv -→ Contains cast and crew details
- movie_data.pkl -→ Preprocessed data (used by the model)

🔗 Link for the Datasets and Preprocessed files :
https://drive.google.com/drive/folders/1SfXjLSxiesLPZodVMg2LAibgVfOzDc3J?usp=drive_link

# Model

- The recommendation engine is powered by cosine similarity
- The .pkl file (movie_data.pkl) stores the processed similarity data
- For each selected movie, the system:
- Finds its similarity scores with all other movies
- Sorts them in descending order
- Returns the Top 10 most similar movies

# Results

- When a user selects a movie:
- The system recommends 10 movies
- Fetches posters using the TMDB API
- Displays them in a clean Streamlit interface

<img width="1855" height="667" alt="Movie" src="https://github.com/user-attachments/assets/c0eee01f-56cc-4352-a056-92c796f85c16" />
