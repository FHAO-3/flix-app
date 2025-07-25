import streamlit as st
from movies.repository import MoviesRepository


class MovieService:
    def __init__(self):
        self.movie_repository = MoviesRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movie_repository.get_movies()
        st.session_state.movies = movies
        return movies

    def create_movie(self, title, release_date, genre, actors, resume):
        movie = dict(
            title=title,
            release_date=release_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        new_movies = self.movie_repository.create_movies(movie=movie)
        st.session_state.movies.append(new_movies)
        return new_movies

    def get_movie_stats(self):
        return self.movie_repository.get_movie_stats()
