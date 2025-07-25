import streamlit as st
import plotly.express as px
from movies.service import MovieService


def show_home():
    movie_service = MovieService()
    movie_stats = movie_service.get_movie_stats()

    st.title('Estatisticas de filmes ')

    if len(movie_stats['movies_by_genre']) > 0:
        fig = px.pie(
            movie_stats['movies_by_genre'],  # data frame dados
            values='count',
            names='genre__name',  # é uma chave dunder que vem da API
            title='Filme por genero'

        )
        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados')  # subtitulo
    st.write(movie_stats['total_movies'])

    st.subheader('Quantidade de Filmes por Genero')
    for genre in movie_stats['movies_by_genre']:
        st.write(f"{genre['genre__name']}: {genre['count']}")

    st.subheader('Total de Avaliações Cadastrados')
    st.write(movie_stats['total_reviews'])

    st.subheader('Media Geral de Estrelas nas Avaliações Cadastrados')
    st.write(movie_stats['average_stars'])
