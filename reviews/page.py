import pandas as pd
import streamlit as st

from st_aggrid import AgGrid
from movies.service import MovieService
from reviews.service import ReviewService


def show_reviews():
    review_service = ReviewService()
    review = review_service.get_reviews()

    if review:
        st.write('Reviews realizadas')
        AgGrid(
            data=pd.json_normalize(review)
        )
    else:
        st.warning('Nenhuma review cadastrada')

    st.divider()

    st.title('Avaliar um filme')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    options_movies = {'Seleciona um filme': 0} | {movie['title']: movie['id'] for movie in movies}
    # select_movie = options_movies.keys()
    selected_movie = st.selectbox(
        label='Escolha um Filme para avaliar',
        options=options_movies
    )

    stars = st.number_input(
        label='Avalia em quantas estrelas este filme',
        min_value=0,
        max_value=5,
        step=1
    )
    resume = st.text_area(label='Deixe seu comentario sobre o filme')

    if st.button('Confirma'):
        new_review = review_service.create_review(
            comment=resume,
            movie=options_movies[selected_movie],
            stars=stars,
        )
        if new_review:
            st.rerun()
        else:
            st.error('Erro ao cadastrar avaliação. Verifique os campos')
