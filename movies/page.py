import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from datetime import datetime
from movies.service import MovieService
from actors.service import ActorsService
from genres.service import GenreService


def show_movies():
    movies_service = MovieService()
    movies = movies_service.get_movies()

    if movies:
        st.write('Lista de filmes')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id'])
        # `.drop` usado para tirar colunas ou linhas
        # foi removido `actors` por ser uma estrutura muito grande para caber dentro de uma celula de tabela
        # tiramos os `id de genres` pois ja temos os generos é na tabela de movies não faz muito sentido

        AgGrid(
            data=movies_df,
            reload_data=True,
            key='movies_grid'
        )
    else:
        st.warning('Não foi encontrado nenhum filme')

    st.title('Cadastrar novos filmes')

    title = st.text_input('Titulo')
    release_date = st.date_input(
        label='Data de nascimanto do filme',
        value=datetime.today(),
        min_value=datetime(1800, 1, 1).date(),  # valor minimo para data
        max_value=datetime.today(),  # valor maximo para data
        format='DD-MM-YYYY'  # modelo de data
    )  # data de lançamento

    genere_service = GenreService()
    genres = genere_service.get_genres()
    genres_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox(
        'Genero do filme',
        list(genres_names.keys())
    )

    actor_service = ActorsService()
    actors = actor_service.get_actors()
    actors_name = {actor['name']: actor['id'] for actor in actors}
    selected_actors_name = st.multiselect(
        'Atores/Atrizes deste filme',
        list(actors_name.keys())
    )  # `multiselect` funciona igual o `selectbox` porem podemos selecionar varias opções
    selected_actors_id = [actors_name[name] for name in selected_actors_name]

    resume = st.text_area('resumo do filme')

    if st.button('Confirma'):
        new_movie = movies_service.create_movie(
            title=title,
            release_date=release_date,
            genre=genres_names[selected_genre_name],
            actors=selected_actors_id,
            resume=resume,
        )
        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao cadastrar o filme. Verifique os campos')
